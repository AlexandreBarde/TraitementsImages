#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkFileDialog import askopenfilename
from skimage import io
from skimage.viewer import ImageViewer
from tkMessageBox import *
from noises.additif import additif
from noises.multiplicatif import multiplicative
from unnoise import moyenneurV1
from noises.saltandpepper import saltandpepper
from unnoise import moyenneurV2
from unnoise import convolution
from unnoise import medianV1
from utils import snr

#Constructeur
class MenuImage(object):

    def __init__(self):
        self._image = "../utils/Lenna.png"
        self._fenetre = Tk()
        self._fenetre.wm_title("Traitements Images")
        self._fenetre['bg'] = 'white'
        self._fenetre.maxsize(width=300, height=200)
        self._fenetre.minsize(width=300, height=200)
        self._menu_bar = Menu(self._fenetre)
        self._fenetre.iconbitmap('../utils/favicon.ico')
        self._generate_menu()
        self._image_bruite = io.imread(self._get_image, as_grey=True)

    def _get_image(self):
        return io.imread(self._image, as_grey=True)

    def _set_image(self, i):
        print "Changement de l'image"
        self._image = i

    def _generate_menu(self):
        p = PanedWindow(self._fenetre, orient=VERTICAL)
        p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
        p.add(Label(p, text='M3202 - Modélisations mathématiques', background='grey', anchor=CENTER))
        p.add(Label(p, text='BARDE Alexandre\nLASSARA Jules', background='white', anchor=CENTER))
        p.add(Label(p, text="Ce projet réalisé dans l'encadrement de\n M. TAHA Abdel-Kaddous et de M. FEHRENBACH \nJerome permet à l'utilisateur de l'application de gérer le \nbruitage et débruitage d'une image qu'il importe.", background='white', anchor=CENTER))
        p.pack()

        menu1 = Menu(self._menu_bar, tearoff=0)
        menu1.add_command(label="Ouvrir image", command=self._open_file)
        menu1.add_command(label="Voir l'image", command=self._see_image)
        menu1.add_command(label="Voir l'image débruitée", command=self._see_image_debruite)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self._fenetre.quit)
        self._menu_bar.add_cascade(label="Fichier", menu=menu1)

        menu2 = Menu(self._menu_bar, tearoff=0)
        menu2.add_command(label="Additif", command=self._additif)
        menu2.add_command(label="Multiplicatif", command=self._multiplicatif)
        menu2.add_command(label="Sel & poivre", command=self._poivre_sel)
        self._menu_bar.add_cascade(label="Bruitage", menu=menu2)

        menu3 = Menu(self._menu_bar, tearoff=0)
        menu3.add_command(label="Médian", command=self._median)
        menu3.add_command(label="Convolution", command=self._convolution)
        menu3.add_command(label="Local V1", command=self._local_v1)
        menu3.add_command(label="Local V2", command=self._local_v2)
        self._menu_bar.add_cascade(label="Débruitage", menu=menu3)

        self._fenetre.config(menu=self._menu_bar)
        self._fenetre.mainloop()


    def _open_file(self):
        newFile = askopenfilename()
        self._image = newFile

    def _see_image(self):
        imageShow = io.imread(self._image, as_grey=True)
        imageViewer = ImageViewer(imageShow)
        imageViewer.show()

    def _see_image_debruite(self):
        imageShow = io.imread(self._see_image_debruite(), as_grey=True)
        imageViewer = ImageViewer(imageShow)
        imageViewer.show()

    def _additif(self):
        showinfo("Information", "Lancement du bruitage additif !")
        imageBruite = additif.additif(self._get_image(), 0.05)
        imageViewer = ImageViewer(imageBruite)
        showinfo("Information", "Bruitage additif terminé !")
        self._image_bruite = imageBruite
        imageViewer.show()

    def _poivre_sel(self):
        showinfo("Information", "Lancement du bruitage sel et poivre !")
        imageBruite = saltandpepper.saltandpepper(self._get_image())
        imageViewer = ImageViewer(imageBruite)
        showinfo("Information", "Bruitage sel et poivre terminé !")
        self._image_bruite = imageBruite
        imageViewer.show()

    def _multiplicatif(self):
        showinfo("Information", "Lancement du bruitage multiplicatif !")
        imageBruite = multiplicative.multiplicative(self._get_image(), 0.1)
        imageViewer = ImageViewer(imageBruite)
        showinfo("Information", "Bruitage multiplicatif terminé !")
        self._image_bruite = imageBruite
        imageViewer.show()

    def _local_v1(self):
        showinfo("Information", "Lancement du débruitage local V1!")
        imageDebruite = moyenneurV1.moyenneur(self._image_bruite)
        imageViewer = ImageViewer(imageDebruite)
        showinfo("Information", "Débruitage local V1 terminé avec un SNR de : " + str(snr.calcsnr(self._get_image(), imageDebruite)) + " dB !")
        imageViewer.show()

    def _local_v2(self):
        showinfo("Information", "Lancement du débruitage local V2 !")
        imageDebruite = moyenneurV2.moyenneur(self._image_bruite)
        imageViewer = ImageViewer(imageDebruite)
        showinfo("Information", "Débruitage local V2 terminé avec un SNR de : " + str(snr.calcsnr(self._get_image(), imageDebruite)) + " dB !")
        imageViewer.show()

    def _convolution(self):
        showinfo("Information", "Lancement du débruitage convolution !")
        imageDebruite = convolution.convolution(self._image_bruite)
        imageViewer = ImageViewer(imageDebruite)
        showinfo("Information", "Débruitage convolution terminé avec un SNR de : " + str(snr.calcsnr(self._get_image(), imageDebruite)) + " dB !")
        imageViewer.show()

    def _median(self):
        showinfo("Information", "Lancement du débruitage médian !")
        imageDebruite = medianV1.median(self._image_bruite)
        imageViewer = ImageViewer(imageDebruite)
        showinfo("Information", "Débruitage médian terminé avec un SNR de : " + str(snr.calcsnr(self._get_image(), imageDebruite)) + " dB !")
        imageViewer.show()
