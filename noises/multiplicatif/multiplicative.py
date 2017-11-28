# -*- encoding: utf-8 -*-

from copy import deepcopy
from numpy import *

"""
Bruitage Multiplicatif
    <image> l'image à bruiter
    <sigma> le sigma du bruitage
    retourne l'image bruitée
"""


def multiplicative(image, sigma):
    noisedimg = deepcopy(image)

    r = random.randn(image.shape[0], image.shape[1])
    r = 1.0 + sigma * r

    # Parcours des lignes de pixels
    for x in range(noisedimg.shape[0]):
        # Parcours des colones de pixels
        for y in range(noisedimg.shape[1]):
            # Remise à la valeur maximale des pixels dépassés
            if noisedimg[x][y] * r[x][y] <= 0.0:
                noisedimg[x][y] = 0.0
            else:
                noisedimg[x][y] = noisedimg[x][y] * r[x][y]

    return noisedimg
