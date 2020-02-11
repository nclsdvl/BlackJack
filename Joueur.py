# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 06:28:56 2020

@author: MonOrdiPro
"""


from Main import Main
    
class Joueur:
    
    def __init__(self, nom, argent):
        self.nom = nom
        self.argent = argent
        self.main = {}
        self.valeurMain = 0
        self.mise = 0
        self.statut = "encore"

        
        
    def setMain(self, main, valeur):
        self.main = Main(main)
        self.valeurMain = valeur
        print("\n"+self.nom + " a en main : " + str(self.main.contenu))
        print("valeur de la main : " + str(self.valeurMain))
    
    def setArgent(self, mise) :
        #print("dans joueur avant setArgent : argent = "+str(self.argent))
        self.argent += mise
        #print("dans joueur apres setArgent : argent = "+str(self.argent))
        
        
    def setStatut(self, statut):
        self.statut = statut
        
    def __repr__(self):
        return "Personne: nom({}), argent({}), main({}), valeurMain({}), statut({}) ".format(
                self.nom, self.argent, self.main, self.valeurMain, self.statut)
    
    def ajoutCarte (self, carte, valeur):
        self.valeurMain += valeur
        self.main.ajoutCarte(carte)
        print("\n"+self.nom + " a maintenant en main : " + str(self.main.contenu)+"\n")
        print("valeur de la main : " + str(self.valeurMain))        
      
    def setMise(self, mise):
        self.mise = mise
        