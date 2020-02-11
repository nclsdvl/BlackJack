# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 06:29:30 2020

@author: MonOrdiPro
"""

class Main:
    
    def __init__(self, main):
        self.contenu = main
    
    def __repr__(self):
        return "{}".format(self.contenu)

    def ajoutCarte(self, carte):
        #print('self.contenu avant = ', self.contenu)
        self.contenu.append(carte)
        #print('self.contenu = apres', self.contenu)