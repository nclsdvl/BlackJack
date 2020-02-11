# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 06:28:19 2020

@author: MonOrdiPro
"""

class Jeu (object):
            
        def __init__(self):
        
            listeCarte = ["As", "Roi", "Dame", "Valet", 10, 9, 8, 7, 6, 5, 4, 3, 2]
            
            monJeu = {}
            for figure in listeCarte:
                monJeu[figure, "pique"] = 0
                monJeu[figure, "coeur"] = 0
                monJeu[figure, "carreau"] = 0
                monJeu[figure, "trefle"] = 0
            monJeu = calculValeur(monJeu)
            
            self.monJeu = monJeu
 

           
            
def calculValeur(jeu):   
    for cle in jeu.keys():
        if type(cle[0]) == int:
            jeu[cle] = cle[0]
        elif cle[0] == "As":
            jeu[cle] = 11
        else :
            jeu[cle] = 10 
    return jeu