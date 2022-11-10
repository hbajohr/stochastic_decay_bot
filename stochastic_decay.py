#!/usr/bin/python

########################################################################
# STOCHASTIC DECAY, Hannes Bajohr 2022                                 #
# Geschrieben für die Poetikvorlesung Hildesheim                       #
# am Literaturhaus St. Jakobi                                          #
#                                                                      #
# STOCHASTIC DECAY unterzieht Theo Lutz' "Stochstische Texte" (1959)   #
# einem zunehmenden Verfall. Je weiter der Monat fortgeschritten ist,  #
# desto mehr Buchstaben der Outputsätze werden durch zufällige andere  #
# Buchstaben ersetzt. Das Ergebnis wird schließlich durch die Text-to- #
# Image-KI Stable Diffusion interpretiert.                             #
########################################################################

from random import choice
from random import randrange
from random import randint
from PIL import Image, ImageFont, ImageDraw 
import tweepy.auth
import requests
import replicate 
import datetime
import logging
import os
import time 

############# Vorbereitungen #############

path = ""  # Wenn kein relativer, sondern absoluter Pfad gewünscht, hier eintragen

# Logfile einrichten
logging.basicConfig(filename=path + "logfile.txt", filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.info("STOCHASTIC DECAY")
logger = logging.getLogger('STOCH_LOG')
logging.warning('------Attempt at sending tweet-------')

# Twitter-Credentials laden - hier entweder eigene Credentials eingeben oder über Umgebungsvariablen lösen
try: 
  CONSUMER_KEY = 'xxxxx'
  CONSUMER_SECRET = 'xxxxx'
  ACCESS_KEY = 'xxxxx'
  ACCESS_SECRET = 'xxxxx'
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
  twitter_API = tweepy.API(auth)
  logging.warning('Twitter successfully authenticated')
except:
  logging.warning('Error while authenticating Twitter')

# Das Modell der Text-to-Image-KI Stable Diffusion laden:
model = replicate.models.get("stability-ai/stable-diffusion")

# Umgebungs für Replicate (siehe https://replicate.com/)
os.environ["REPLICATE_API_TOKEN"]="xxxxxxxxx"

# Die Listenobjekte mit den Satzelementen erstellen
subjekt = [['GRAF', 0], ['FREMDE', 1], ['BLICK',0],['KIRCHE',1], ['SCHLOSS',2], ['BILD',2], ['AUGE',2], ['DORF',2], ['TURM',0], ['BAUER',0], ['WEG',0], ['GAST',0], ['TAG',0], ['HAUS',2], ['TISCH',0], ['KNECHT',0]]
adjektiv = ['OFFEN', 'STILL', 'STARK', 'GUT', 'SCHMAL', 'NAH', 'NEU', 'LEISE', 'FERN', 'TIEF', 'SPÄT', 'DUNKEL', 'FREI', 'GROSS', 'ALT', 'WÜTEND']
konjunktion = [' UND', ' ODER', ' SO GILT', '.', '.', '.', '.', '.']
operator = [['EIN', 'EINE', 'EIN'], ['JEDER', 'JEDE', 'JEDES'], ['KEIN', 'KEINE', 'KEIN'], ['NICHT JEDER', 'NICHT JEDE', 'NICHT JEDES']]

# Übersetzer initialisieren
try:
  import translators as ts
  translate=True
  logging.warning('Translator successfully imported')
except: 
  translate=False
  logging.warning('Error importing translator')

############# Funktionen definieren #############

def tweet_image(image_path, message):
    twitter_API.update_status_with_media(message, image_path)

def phrase():  #setzt Satz zusammen
  wahl_subjekt = choice(subjekt) 
  wahl_operator = choice(operator)
  wahl_operator = wahl_operator[wahl_subjekt[1]]
  wahl_subjekt = wahl_subjekt[0]
  text = wahl_operator + ' ' +  wahl_subjekt 
  return text + ' IST'

def decay_word(word):  #lässt Wort zerfallen
  zahl = randrange(len(word))
  output = ''
  for i in range (0, len(word)):
    if i == zahl:
      output = output + chr(randint(65, 90))
    else:
      output = output + word[i]
  return output

def decay_category():  #wählt Kategorie, in der Wort zerfallen soll
  d = int(datetime.datetime.now().strftime("%d")) 
  for i in range(0,d*3):
    test = randint(0,3)
    if test == 0: # subjekt
      sample = randrange(0,len(subjekt))
      subjekt[sample][0] = decay_word(subjekt[sample][0])
    elif test == 1: # adjektiv
      sample = randrange(0,len(adjektiv))
      adjektiv[sample] = decay_word(adjektiv[sample])
    elif test == 2: # konjunktion
      sample = randrange(0,2)
      konjunktion[sample] = decay_word(konjunktion[sample])
    elif test == 3: # operator
      sample = randrange(0,len(operator))
      test2 = randint(0,2)
      operator[sample][test2] = decay_word(operator[sample][test2])
      
def make_diffusion_image(input):  #wandelt Satz in Bild um
  try: 
    img_file = model.predict(prompt=input)
    print(img_file)
    time.sleep(3)
    #logging.warning('Replicate successfully used for image generation')
    print('Replicate successfully used for image generation')
    try:
      r = requests.get(img_file[0], allow_redirects=True)
      open(path + 'img/out_diff.png', 'wb').write(r.content)
      logging.warning("Copied image to server")
    except:
      logging.warning("Couldn't copy image to server")
  except:
    logging.warning('Error using Replicate')

def make_text_overlay_image(input):  #legt Text über Bild; stellt sicher, dass Text umgebrochen wird
  if input[:-1].find(".") != -1:
    input = input[0:(input.find(".")+1)] + "\n" + input[(input.find(".")+2):]
  elif input[:-1].find(".") == -1:
    haelfte = round(len(input)/2)-1
    for i in range(0,7):
      if input[haelfte] == " ":
        input = input[0:haelfte] + "\n" + input[haelfte+1:]
        break
      haelfte = haelfte+1
  x, y = 15,365
  my_image = Image.open(path + "img/out_diff.png")

  #Textumrandung, damit Text auch auf hellem Hintergrund lesbar ist
  image_editable = ImageDraw.Draw(my_image)
  font = ImageFont.truetype(path + "font/ActionCondLight.ttf", 70)
  image_editable.text((x-1, y), input, font=font, fill="black")
  image_editable.text((x+1, y), input, font=font, fill="black")
  image_editable.text((x, y-1), input, font=font, fill="black")
  image_editable.text((x, y+1), input, font=font, fill="black")
  image_editable.text((x, y), input, font=font, fill="white")
  try:
    my_image.save(path + "img/out_result.jpg")
    logging.warning('Overlay image successfully saved')
  except:
    logging.warning('Error saving overlay image')

def choose_style(): # Aus dieser Liste werden Stile ausgewählt und dem Output-Satz angehängt, bevor sie Replicate übergeben werden
  styles = [", in a 1950s advertising style", ", in a photorealistic style", ", in steampunk style", ", in vaporware style", 
            ", in the style of an impressionist painting", ", in the style of a technical drawing", ", in the style of TRON", 
            ", drawn in the style of typewriter art", ", grainy super 8", ", as embroidery", ", as a 3D rendering", ", concept art",
            ", in the style of a 1990s ad", ", in the style of a black and white Dürer etching", ", in the style of a woodprint", 
            ", in the style of a dot matrix printout", ", in a futurist style", ", drawn with magic markers", ", as a polaroid"
            ", in the style of an elaborate graffiti", ", in a Renaissance style", ", bioluminescence", ", 4k octane render",
            ", trending on Artstation", ", HQ masterpiece"] 
  return choice(styles)
  
  
########## Hauptprogramm ##########

decay_category()
output = (phrase() + ' ' + choice(adjektiv) + choice(konjunktion) + ' ' +  phrase() + ' ' +  choice(adjektiv) + '.')  
logging.warning('Original message: ' + output)
output_original = output
if translate:
  output = ts.google(output)
  logging.warning('Message successfully translated: ' + output)
else:
  logging.warning('Message not translated') 
try: 
  chosen_style = choose_style()
  make_diffusion_image(output[:-1] + chosen_style)
  logging.warning("STYLE:" + chosen_style[1:])
except:
  logging.warning('Error making diffusion image')
try:
  make_text_overlay_image(output_original)
except: 
  logging.warning('Error making overlay')
try:
  tweet_image(path + "img/out_result.jpg", output_original + "\n[𝔡𝔢𝔠𝔞𝔶 𝔯𝔞𝔱𝔢: " + str(int(datetime.datetime.now().strftime("%d"))) + "]")
  logging.warning('------Tweet successfully sent------')
except:
  logging.warning('------ERROR SENDING TWEET------')
