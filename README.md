# Traitements d'images

Dans le cadre d'un projet universitaire nous devions travailler sur une application permettant de *bruiter* / *débruiter* une image car une photographie peut se détériorer de diverses façons, la copie (scan) ou même par le temps.
Donc ce projet consiste donc à *rétablir* ou à *améliorer* la qualité d'une image en noir et blanc.

Pour évaluer la qualité des différents débruitages qui sont effectués nous utilisons le _Rapport Signal sur Bruit_ (Signal to Noise Ratio en anglais).

## Bruitages 

Voici les différents bruitages disponibles dans cette application :

_(/noises/nomdubruitage)_

* Additif
* Multiplicatif
* Poivre et sel

## Débruitages

Voici les différents débruitages disponibles dans cette application:

_(/unoise/nomdudébruitage)_

* Convolution
* Median V1 et V2
* Moyenneur V1 et V2

## Menu

Pour utiliser le menu graphique il suffit de lancer le fichier "lancement.py" qui permet de créer un objet Menu.

## Images

#### Bruitage additif

![alt text](output/additif.jpg?raw=true "Bruitage additif")

#### Bruitage multiplicatif

![alt text](output/additif.jpg?raw=true "Bruitage multiplicatif")

#### Bruitage sel et poivre

![alt text](output/bruite.jpg?raw=true "Bruitage sel et poivre")

#### Débruitage par filtrage médian sur bruitage sel et poivre V1

![alt text](output/debruitageMedianV1.jpg?raw=true "Débruitage par filtrage médian sur bruitage sel et poivre V1")

#### Débruitage par filtrage médian sur bruitage sel et poivre V2

![alt text](output/debruitageMedianV2.jpg?raw=true "Débruitage par filtrage médian sur bruitage sel et poivre V2")
