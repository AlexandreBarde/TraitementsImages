from numpy import *


# Methode de calcul SNR

def calcsnr(origin, unnoised):
    som1 = 0.0
    som2 = 0.0
    for i in range(origin.shape[0]):
        for y in range(origin.shape[1]):
            som1 = som1 + (origin[i][y])**2
            som2 = som2 + (unnoised[i][y] - (origin[i][y]))**2
    return 10*log10(som1/som2)
