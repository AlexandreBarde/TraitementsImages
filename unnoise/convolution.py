# -*- encoding: utf-8 -*-

from copy import deepcopy
from numpy import *

"""
Débruitabe par filtrage par convolution
    <image> l'image à débruiter
    retourne l'image débruitée
"""


def convolution(image):
    unnoisedimg = deepcopy(image)

    # Parcours des lignes de pixels
    for i in range(unnoisedimg.shape[0]):
        # Parcours des colones de pixels
        for j in range(unnoisedimg.shape[1]):
            # Récupération du noyau
            noyau = pixelsAround(unnoisedimg, i, j)
            # Application de la matrice de 1/9
            noyau = noyau / 9.0
            # Application de la matrice augmentant le contraste
            noyau[1][1] = 5 * noyau[1][1] - noyau[0][1] - noyau[1][0] - noyau[1][2] - noyau[2][1]
            # Modification du pixel courant
            unnoisedimg[i][j] = sum(noyau)
    return unnoisedimg


"""
Méthode permettant de récupérer une matrice de 3×3 pixels autour du pixel (x,y)
"""


def pixelsAround(image, x, y):
    p1 = 0.0
    p2 = 0.0
    p3 = 0.0
    p4 = 0.0
    p5 = 0.0
    p6 = 0.0
    p7 = 0.0
    p8 = 0.0
    if image.shape[0] - 1 >= x - 1 >= image.shape[0] - 1 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        p1 = image[x - 1][y - 1]
    if image.shape[0] - 1 >= x - 1 >= 0:
        p2 = image[x - 1][y]
    if image.shape[0] - 1 >= x - 1 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        p3 = image[x - 1][y + 1]
    if image.shape[1] - 1 >= y - 1 >= 0:
        p4 = image[x][y - 1]
    if image.shape[1] - 1 >= y + 1 >= 0:
        p5 = image[x][y + 1]
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y - 1 >= 0:
        p6 = image[x + 1][y - 1]
    if image.shape[0] - 1 >= x + 1 >= 0:
        p7 = image[x + 1][y]
    if image.shape[0] - 1 >= x + 1 >= 0 and image.shape[1] - 1 >= y + 1 >= 0:
        p8 = image[x + 1][y + 1]

    values = array([[p1, p2, p3],
              [p4, image[x][y], p5],
              [p6, p7, p8]])
    return values