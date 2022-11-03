# Stochastic Decay Bot

Dieser Bot ist für meine Poetikvorlesung an der Universität Hildesheim geschrieben worden.  

Der Stochastic Decay-Bot bringt zwei Paradigmen digitaler Literatur zusammen - das regelbasierte "sequentielle Paradigma" und das auf neuronalen Netzen beruhende "konnektionistische Paradigma". Als solches ist er sowohl ein Werk der Literatur/digitalen Kunst als auch eine Illustration der Geschichte der digitalen Literatur.

Der Bot zitiert das allererste deutschsprachige Werk digitaler Literatur: Theo Lutz' "Stochastische Texte" von 1959, die unter der Leitung von Max Bense entstanden. Das Programm produzierte zufällig zusammengesetzte Sätze aus einem Satz von Wörtern aus Kafkas ''Schloss''. 

Für meine Version geschehen zwei Aktualisierungen: Erstens passe ich Lutz' Original den Möglichkeiten eines Twitterbots an, indem ich ihn dynamisieren: Je nach Tag des Monats wird der generierte Text "korrumpiert" (Buchstaben austauscht), so dass am Monatsende der Lutz'sche Text fast unlesbar wird. Zweitens verbinde ich das regelbasierte alte Paradigma mit einem neuronalen Netz zur Bildgenerierung (stable diffusion), die den Satz versucht als Bild zu interpretieren. Auch das wird, je nach Verlauf des Monats, immer schwerer. 

Der Programmcode ist frei verfügbar; nur die API-Keys für tweepy und reproduce müssen in den Code eingetragen werden (oder besser noch als Umgebungsvariablen gespeichert werden).
