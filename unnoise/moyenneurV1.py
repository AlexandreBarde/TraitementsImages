# -*- encoding: utf-8 -*-

from copy import deepcopy

"""
Débruitabe par filtrage moyenneur sur les pixels noirs et blancs sur une matrice de 3×3
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


def moyennePixel(image, x, y):
    nombrepixels = 0.0
    p1 = 0.0
    p2 = 0.0
    p3 = 0.0
    p4 = 0.0
    p5 = 0.0
    p6 = 0.0
    p7 = 0.0
    p8 = 0.0
    if image.shape[0]-1 >= x-1 >= image.shape[0]-1 >= 0 and image.shape[1]-1 >= y-1 >= 0:
        p1 = image[x-1][y-1]
        nombrepixels = nombrepixels + 1
    if image.shape[0]-1 >= x-1 >= 0:
        p2 = image[x-1][y]
        nombrepixels = nombrepixels + 1
    if image.shape[0]-1 >= x-1 >= 0 and image.shape[1]-1 >= y + 1 >= 0:
        p3 = image[x-1][y+1]
        nombrepixels = nombrepixels + 1
    if image.shape[1]-1 >= y-1 >= 0:
        p4 = image[x][y-1]
        nombrepixels = nombrepixels + 1
    if image.shape[1]-1 >= y+1 >= 0:
        p5 = image[x][y+1]
        nombrepixels = nombrepixels + 1
    if image.shape[0]-1 >= x+1 >= 0 and image.shape[1]-1 >= y - 1 >= 0:
        p6 = image[x+1][y-1]
        nombrepixels = nombrepixels + 1
    if image.shape[0]-1 >= x+1 >= 0:
        p7 = image[x+1][y]
        nombrepixels = nombrepixels + 1
    if image.shape[0]-1 >= x+1 >= 0 and image.shape[1]-1 >= y + 1 >= 0:
        p8 = image[x+1][y+1]
        nombrepixels = nombrepixels + 1
    moyenne = (p1+p2+p3+p4+p5+p6+p7+p8)/nombrepixels
    return moyenne