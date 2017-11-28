# -*- encoding: utf-8 -*-

from copy import deepcopy
from numpy import *


"""
Débruitage par filtrage médian
    <image> l'image à débruiter
    retourne l'image débruitée
"""


def median(image):
    nombrePixel = 0
    newimg = deepcopy(image)
    # Parcours des lignes de pixels
    for x in range(newimg.shape[0]):
        # Parcours des colonnes de pixels
        for y in range(newimg.shape[1]):
            newimg[x][y] = getPixels(newimg, x, y)
            if(image[x][y] == newimg[x][y]):
                nombrePixel = nombrePixel + 1
    #print("Nombre de pixels non modifies : " + str(nombrePixel))
    #print("Pourcentage de pixels non modifes : " + str(image.shape[0]*image.shape[1]/nombrePixel) + str(" %"))
    return newimg


# Il faut prendre les 8 pixels qui sont autours du pixel sur lequel nous travaillons
# Il faut ranger les pixels par valeurs croissantes
# Et ensuite prendre la mediane de cette liste ordonnee



"""
Image: Image sur laquelle nous travaillons
x : position x du pixel
y : position y du pixel
return : retourne une liste qui contient les 8 pixels autours du pixel sur lequel nous travaillons
"""


def getPixels(image, x, y):

    liste = zeros(8, float)

    if image.shape[0] - 1 >= x - 1 >= image.shape[0] - 1 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        liste[0] = image[x - 1][y - 1]
    if image.shape[0] - 1 >= x - 1 >= 0:
        liste[1] = image[x - 1][y]
    if image.shape[0] - 1 >= x - 1 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        liste[2] = image[x - 1][y + 1]
    if image.shape[1] - 1 >= y - 1 >= 0:
        liste[3] = image[x][y - 1]
    if image.shape[1] - 1 >= y + 1 >= 0:
        liste[4] = image[x][y + 1]
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        liste[5] = image[x + 1][y - 1]
    if image.shape[0] - 1 >= x + 1 >= 0:
        liste[6] = image[x + 1][y]
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        liste[7] = image[x + 1][y + 1]

    # Permet de trier notre liste
    liste = sorted(liste)

    mediane = (liste[3] + liste[4]) / 2.0

    # Retourne la mediane (8 pixels donc 8/2 = 4)
    return mediane