
# -*- encoding: utf-8 -*-

from copy import deepcopy
from numpy import *

"""
Débruitabe par filtrage moyenneur sur les pixels noirs et blancs sur une matrice de 5×5
    <image> l'image à débruiter
    retourne l'image débruitée
"""


def moyenneur(image):
    newimg = deepcopy(image)
    for x in range(newimg.shape[0]):
        for y in range(newimg.shape[1]):
            if newimg[x][y] == 0 or newimg[x][y] == 1:
                newimg[x][y] = moyennePixel(newimg, x, y)
    return newimg


# Calcule la moyenne des pixels d'une image

def moyennePixel(image, x, y):
    values = zeros(26, float)

    if image.shape[0] - 1 >= x - 1 >= image.shape[0] - 1 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        values[1] = image[x - 1][y - 1]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x - 1 >= 0:
        values[2] = image[x - 1][y]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x - 1 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        values[3] = image[x - 1][y + 1]
        values[0] = values[0] + 1
    if image.shape[1] - 1 >= y - 1 >= 0:
        values[4] = image[x][y - 1]
        values[0] = values[0] + 1
    if image.shape[1] - 1 >= y + 1 >= 0:
        values[5] = image[x][y + 1]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        values[6] = image[x + 1][y - 1]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x + 1 >= 0:
        values[7] = image[x + 1][y]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        values[8] = image[x + 1][y + 1]
        values[0] = values[0] + 1
    # Version 2
    if image.shape[0] - 1 >= x - 2 >= 0 and image.shape[1] - 1 >= y - 2 >= 0:
        values[10] = image[x - 2][y - 2]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x - 2 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        values[11] = image[x - 2][y - 1]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x - 2 >= 0:
        values[12] = image[x - 2][y]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x - 2 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        values[13] = image[x - 2][y + 1]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x - 2 >= 0 and image.shape[1] - 1 >= y + 2 >= 0:
        values[14] = image[x - 2][y + 2]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x - 1 >= 0 and image.shape[1] - 1 >= y - 2 >= 0:
        values[15] = image[x - 1][y - 2]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x - 1 >= 0 and image.shape[1] - 1 >= y + 2 >= 0:
        values[16] = image[x - 1][y - 2]
        values[0] = values[0]+ 1
    if image.shape[1] - 1 >= y - 2 >= 0:
        values[17] = image[x][y - 2]
        values[0] = values[0] + 1
    if image.shape[1] - 1 >= y + 2 >= 0:
        values[18] = image[x][y + 2]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] >= y - 2 >= 0:
        values[19] = image[x][y - 2]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y + 2 >= 0:
        values[20] = image[x + 1][y + 2]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x + 2 >= 0 and image.shape[1] - 1 >= y - 2 >= 0:
        values[21] = image[x + 2][y - 2]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x + 2 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        values[22] = image[x + 2][y - 1]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x + 2 >= 0:
        values[23] = image[x + 2][y]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x + 2 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        values[24] = image[x + 2][y + 1]
        values[0] = values[0] + 1
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y + 2 >= 0:
        values[25] = image[x + 1][y + 2]
        values[0] = values[0] + 1
    moyenne = (sum(values) - values[0]) / values[0]
    return moyenne