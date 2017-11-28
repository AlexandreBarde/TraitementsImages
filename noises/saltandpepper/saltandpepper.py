# -*- encoding: utf-8 -*-

import random
from copy import deepcopy

"""
Bruitage Sel & Poivre
    <image> l'image à bruiter
    retourne l'image bruitée
"""


def saltandpepper(image):
    noisedimg = deepcopy(image)
    # Parcours des lignes de pixels
    for i in range(noisedimg.shape[0]):
        # Parcours des colones de pixels
        for y in range(noisedimg.shape[1]):
            # Generation d'un chiffre random entre 0.0 et 1.0
            rand = random.random()
            # Pour 5% de chance, le pixel (i,j) devient blanc
            if rand < 0.05:
                noisedimg[i][y] = 1
            # Pour 5 autre % de chance, le pixel (i,j) devient noir
            elif rand < 0.10:
                noisedimg[i][y] = 0
    # Retourne l'image
    return noisedimg