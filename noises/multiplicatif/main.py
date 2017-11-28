# -*- encoding: utf-8 -*-

from skimage import io
from skimage.viewer import ImageViewer

from unnoise.convolution import convolution
from noises.multiplicatif.multiplicative import multiplicative

# MULTIPLICATIVE NOISE

# Lecture de l'image
lenna = io.imread("../../utils/Lenna.png", as_grey=True)
blenna = multiplicative(lenna, 0.1)
viewer = ImageViewer(blenna)
# viewer = ImageViewer(lenna)
viewer.show()
viewer2 = ImageViewer(convolution(blenna))
viewer2.show()
