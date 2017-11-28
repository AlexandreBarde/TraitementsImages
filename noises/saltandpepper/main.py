# -*- encoding: utf-8 -*-

from noises.saltandpepper.saltandpepper import saltandpepper
from numpy import *
from skimage import io
from skimage.viewer import ImageViewer

from unnoise.moyenneurV2 import moyenneur
from utils.snr import calcsnr

# Lecture de l'image
lenna = io.imread("../../utils/Lenna.png", as_grey=True)

# Bruitage de l'image
noisedlenna = saltandpepper(lenna)

print("SNR du debruitage : " + str(round(calcsnr(lenna, moyenneur(noisedlenna)), 2)) + "dB")

# Affichage de l'image bruitee puis debruitee
viewer = ImageViewer(noisedlenna)
viewer.show()
viewer2 = ImageViewer(moyenneur(noisedlenna))
viewer2.show()

# Stockage des images dans le dossier output
# viewer.save_to_file('output/bruite.jpg')
# viewer2.save_to_file('output/debruitage.jpg')
