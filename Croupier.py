# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 06:28:40 2020

@author: MonOrdiPro
"""

# format de self.jeu.monJeu  --> {('As', 'pique'): 11, ('As', 'coeur'): 11, ...}

from Jeu import Jeu
from Main import Main
import random

class Croupier():
    def __init__(self):
        print("Croupier en place")
        self.jeu = Jeu()
        self.main = {}
        self.valeurMain = 0
        
    def setMain(self, main, valeur1, valeur2):
        self.main = Main(main)
        self.valeurMain = valeur1 + valeur2
        print("\nle croupier a en main : " + str(self.main.contenu[0]))
        print("valeur de la main : " + str(valeur1))
        
    def ajoutCarte (self, carte, valeur):
        self.valeurMain += valeur
        self.main.ajoutCarte(carte)
        print("\n Le croupier a maintenant en main : " + str(self.main.contenu)+"\n")
        print("valeur de la main : " + str(self.valeurMain))            

    def distribuerPremiereMain(self, joueurs):
        
        for joueur in joueurs:
            tirer_2_carte(joueur, self.jeu)
        
        tirer_2_carte(self, self.jeu)        
    
    def tirer_1_carte(self, joueur, jeu):
        carte_1_joueur = random.choice(list(jeu.monJeu.keys()))
        valeur1 = jeu.monJeu[carte_1_joueur]
        del jeu.monJeu[carte_1_joueur]
        joueur.ajoutCarte(carte_1_joueur, valeur1)  
        
        if str(type(joueur)) == "<class 'Croupier.Croupier'>":
            print("le joueur tire la carte : " + str(carte_1_joueur))
    
    

def tirer_2_carte(joueur, jeu):

    carte_1_joueur = random.choice(list(jeu.monJeu.keys()))
    valeur1 = jeu.monJeu[carte_1_joueur]
    del jeu.monJeu[carte_1_joueur]
    carte_2_joueur = random.choice(list(jeu.monJeu.keys()))
    valeur2 = jeu.monJeu[carte_2_joueur]
    del jeu.monJeu[carte_2_joueur]
    
    valeur_main = valeur1 + valeur2
    
    maMain = [carte_1_joueur, carte_2_joueur]
    if str(type(joueur)) == "<class 'Croupier.Croupier'>":
        joueur.setMain(maMain, valeur1, valeur2)
    else:
        joueur.setMain(maMain, valeur_main)



