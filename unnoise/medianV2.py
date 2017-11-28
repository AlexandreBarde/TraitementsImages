# -*- encoding: utf-8 -*-

from copy import deepcopy
from numpy import *

"""
Débruitabe par filtrage médian
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

    liste = zeros(24, float)

    if image.shape[0] - 1 >= x - 1 >= image.shape[0] - 1 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        liste[0] = image[x - 1][y - 1]
        print("0" + str(liste[0]))
    if image.shape[0] - 1 >= x - 1 >= 0:
        liste[1] = image[x - 1][y]
        print("1 : " + str(liste[1]))
    if image.shape[0] - 1 >= x - 1 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        liste[2] = image[x - 1][y + 1]
        print("2 : " + str(liste[2]))
    if image.shape[1] - 1 >= y - 1 >= 0:
        liste[3] = image[x][y - 1]
        print("3 : " + str(liste[3]))
    if image.shape[1] - 1 >= y + 1 >= 0:
        liste[4] = image[x][y + 1]
        print("4 : " + str(liste[4]))
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        liste[5] = image[x + 1][y - 1]
        print("5 : " + str(liste[5]))
    if image.shape[0] - 1 >= x + 1 >= 0:
        liste[6] = image[x + 1][y]
        print("6 : " + str(liste[6]))
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        liste[7] = image[x + 1][y + 1]
        print("7 : " + str(liste[7]))
    if image.shape[0] - 1 >= x - 2 >= 0 and image.shape[1] - 1 >= y - 2 >= 0:
        liste[8] = image[x - 2][y - 2]
        print("8 : " + str(liste[8]))
    if image.shape[0] - 1 >= x - 2 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        liste[9] = image[x - 2][y - 1]
        print("9 : " + str(liste[9]))
    if image.shape[0] - 1 >= x - 2 >= 0:
        liste[10] = image[x - 2][y]
        print("10 : " + str(liste[10]))
    if image.shape[0] - 1 >= x - 2 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        liste[11] = image[x - 2][y + 1]
        print("11 : " + str(liste[11]))
    if image.shape[0] - 1 >= x - 2 >= 0 and image.shape[1] - 1 >= y + 2 >= 0:
        liste[12] = image[x - 2][y + 2]
        print("12 : " + str(liste[12]))
    if image.shape[0] - 1 >= x - 1 >= 0 and image.shape[1] - 1 >= y - 2 >= 0:
        liste[13] = image[x - 1][y - 2]
        print("13 : " + str(liste[13]))
    if image.shape[0] - 1 >= x - 1 >= 0 and image.shape[1] - 1 >= y + 2 >= 0:
        liste[14] = image[x - 1][y - 2]
        print("14 : " + str(liste[14]))
    if image.shape[1] - 1 >= y - 2 >= 0:
        liste[15] = image[x][y - 2]
        print("15 : " + str(liste[15]))
    if image.shape[1] - 1 >= y + 2 >= 0:
        liste[16] = image[x][y + 2]
        print("16 : " + str(liste[16]))
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] >= y - 2 >= 0:
        liste[17] = image[x][y - 2]
        print("17 : " + str(liste[17]))
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y + 2 >= 0:
        liste[18] = image[x + 1][y + 2]
        print("18 : " + str(liste[18]))
    if image.shape[0] - 1 >= x + 2 >= 0 and image.shape[1] - 1 >= y - 2 >= 0:
        liste[19] = image[x + 2][y - 2]
        print("19 : " + str(liste[19]))
    if image.shape[0] - 1 >= x + 2 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        liste[20] = image[x + 2][y - 1]
        print("20 : " + str(liste[20]))
    if image.shape[0] - 1 >= x + 2 >= 0:
        liste[21] = image[x + 2][y]
        print("21 : " + str(liste[21]))
    if image.shape[0] - 1 >= x + 2 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        liste[22] = image[x + 2][y + 1]
        print("22 : " + str(liste[22]))
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y + 2 >= 0:
        liste[23] = image[x + 1][y + 2]
        print("23 : " + str(liste[23]))

    # Permet de trier notre liste
    liste = sorted(liste)

    mediane = (liste[11] + liste[12]) / 2.0

    # Retourne la mediane (8 pixels donc 12/13 = 4)
    return mediane