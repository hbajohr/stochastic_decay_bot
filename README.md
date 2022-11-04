# Stochastic Decay Bot ([@JTOCHAST_TFXFE](https://twitter.com/JTOCHAST_TFXFE)

### Was ist das?
Diesen Bot habe ich für die Poetikvorlesung an der Universität Hildesheim (15. November 2022) geschrieben.  

### Was soll das?
Der Stochastic Decay-Bot bringt zwei Paradigmen digitaler Literatur zusammen - das regelbasierte »sequenzielle Paradigma« und das auf neuronalen Netzen beruhende »konnektionistische Paradigma«. Während die meisten Computerprogramme zum ersten gehören (sie sind Listen mit Anweisungen, die sequenziell abgearbeitet werden und die für Menschen lesbar sind), gehören moderne KI-Modelle zu letzterem (und sind eben nicht mehr lesbar, sondern undurchsichtige Black Boxes). Eine genaue Erklärung findet sich [hier](https://hannesbajohr.de/wp-content/uploads/2021/09/Kunstliche_Intelligenz_und_digitale_Lite.pdf). Der Bot ist daher sowohl ein _Werk_ der digitalen Literautr als auch eine _Illustration_ ihrer Geschichte.

### Was bedeutet der Text?
Der Bot zitiert das allererste deutschsprachige Werk digitaler Literatur: Theo Lutz' [»Stochastische Texte«]([https://www.google.com](https://zkm.de/de/werk/stochastische-texte) von 1959, die unter der Leitung von Max Bense entstanden. Das Programm produzierte zufällig zusammengesetzte Sätze aus einem Satz von Wörtern aus Kafkas _Schloss_. Zum Beispiel: JEDES DORF IST GROSS. EIN BAUER IST LEISE. 

![Twitter-Bot-Bild](https://user-images.githubusercontent.com/20578427/199972653-19b125a7-aecd-481f-8c7e-24e13c25964b.png "Ausschnitt aus den originalen Stochastischen Texten")


### Was ist daran neu?
Für meine Version habe ich zwei Aktualisierungen vorgenommen: 
Erstens passe ich Lutz' Original den Möglichkeiten eines Twitterbots an, indem ich ihn _dynamisiere_: Je nach Tag des Monats wird der generierte Text Schritt für Schritt »korrumpiert« (Buchstaben werden zufällig austauscht, so dass aus SCHLOSS irgendwann vielleicht SXHLOTS wird). Der Lutz'sche Text ist so am Monatsende fast unlesbar. Der Reset erfolgt immer am Monatsanfang.
Zweitens verbinde ich das alte _regelbasierte_ Paradigma mit einem neuen _neuronalen Netz_ zur Bildgenerierung (der Text-to-Image-KI »stable diffusion«, siehe dazu [hier](https://en.wikipedia.org/wiki/Stable_Diffusion)), die den Satz versucht als Bild zu interpretieren. 
Damit vermischt der Bot drittens nicht das alte und das neue Paradigma, sondern illustriert ihre Besonderheiten über die Funktion von _Fehlern_: Während im sequenziellen Paradigma ein Fehler klar erkennbar ist – ein falscher Buchstabe ruiniert die Bedeutung des Wortes –, ist das konnektionistische Paradigma sehr viel flexibler und versucht, Fehler zu glätten und dennoch Sinn aus der sinnlosen Eingabe zu erzeugen. Es bevorzugt, könnte man sagen, glatte Oberflächen und die Kohärenz von Gestalten statt Brüche zuzulassen und Fehler offenzulegen. 

![Beispielbild des Twitterbots: Ein mysteriöses schwarz-weißes Bild mit der Aufschrift: JEDER WEG IST DUNKEL. EIN GAAF IST FERN.](https://user-images.githubusercontent.com/20578427/199972653-19b125a7-aecd-481f-8c7e-24e13c25964b.png "JEDER WEG IST DUNKEL. EIN GAAF IST FERN.")

### Wie kann ich das selbst laufen lassen?
Der Programmcode ist frei verfügbar; nur die API-Keys für tweepy und relicate müssen in den Code eingetragen werden (oder besser noch als Umgebungsvariablen gespeichert werden).
