# -*- encoding: utf-8 -*-

from copy import deepcopy
from numpy import *

"""
Bruitage Additif
    <image> l'image à bruiter
    <sigma> le sigma du bruitage
    retourne l'image bruitée
"""


def additif(image, sigma):
    noisedimg = deepcopy(image)

    # Image bruitee = image de base + sigma (matrice aleatoire)
    matriceRdm = sigma * random.randn(noisedimg.shape[0], noisedimg.shape[1])

    # Parcours des lignes de pixels
    for x in range(noisedimg.shape[0]):
        # Parcours des lignes de pixels
        for y in range(noisedimg.shape[1]):
            if noisedimg[x][y] + matriceRdm[x][y] <= 0.0:
                noisedimg[x][y] = 0.0
            else:
                noisedimg[x][y] = noisedimg[x][y] + matriceRdm[x][y]

    return noisedimg


