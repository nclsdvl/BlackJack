# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 06:52:43 2020

@author: MonOrdiPro
"""

import sys
import time
from Joueur import Joueur
from Croupier import Croupier


class Partie:
    
    """
    Classe contenant l'algo principal du jeu de blackjack --> initialisationPartie ()
    
    attributs : 
        Nbr de place sur la table
        nbr joueur inscrit
        liste de ces joueurs.
    
    
    TODO / BUG :
        
        
        --> remove joueur ne check pas tous les jouer???????? (l 258)
            

            

        

    """

    def __init__(self):
        self.nbr_placeDispo = 8
        self.nbr_joueur = 0
        self.liste_de_joueur = []
    

    def initialisationPartie(self):
        print("Bienvenue au jeu de BlackJack")
        croupier = Croupier()
        endGame = False
        rejouer = True
        

        # 1. initialisation et creation des joueurs :
        while self.nbr_joueur < 1 and rejouer == True:
            
            entre = input("Combien de joueur réel souhaitez vous ajouter? (max 8)\n")
            if entre == "quit":
                sys.exit()
            try:
                self.nbr_joueur = int(entre)
            except :
                print("Merci d'entrer un nombre entre 1 et " + str(self.nbr_placeDispo))
                continue
            if self.nbr_joueur > self.nbr_placeDispo :
                self.nbr_joueur = 0
                print("Vous ne pouvez pas entrer plus de 5 joueurs... essaye encore !")
            elif self.nbr_joueur < 1 :
                print("Merci d'entrer un nombre entre 1 et " + str(self.nbr_placeDispo))
    
                    
            creationJoueur(self, self.nbr_joueur)
            
            
            # 2. mise des joueurs, distribution de la premiere main, verification des blackJack...
            while rejouer == True :
                rejouer == False
                miser(self.liste_de_joueur)
                
                croupier.distribuerPremiereMain(self.liste_de_joueur)
                
                checkScore(self.liste_de_joueur) 
                
                endGame = checkEndGame(self.liste_de_joueur, croupier)
                
                # 3 . gestion du tirage des nouvelles cartes pour les joueurs qui le souhaitent
                while endGame == False :
                
                    for joueur in self.liste_de_joueur:
                        if joueur.statut == "encore" :
                            bonneEntree = False
                            a=""
                            while bonneEntree == False :
                                print("rappel "+ joueur.nom +" votre main = "+str(joueur.main))
                                print("valeur de la main = "+str(joueur.valeurMain) + " VS valeur du croupier = " + str(croupier.valeurVisible))
                                time.sleep(2)
                                a = input( joueur.nom + " voulez vous tirez une nouvelle carte (o ou n) : ")
                                if a=="n":
                                    joueur.setStatut("stop")
                                    bonneEntree = True
                                elif a=="o":
                                    #print("on continu")
                                    croupier.tirer_1_carte(joueur, croupier.jeu)
                                    bonneEntree = True
                    
        
                    # mise a jour des scores   
                    checkScore(self.liste_de_joueur)

                    
                    endGame = checkEndGame(self.liste_de_joueur, croupier)
                    

                                   
                input_rejouer = input("voulez-vous rejouer ? (o pour oui, n pour non) ")
                bonChoix = False
                

                

                
                while bonChoix == False :
                    if input_rejouer == "o":
                        removeJoueur (self.liste_de_joueur)
                        bonChoix = True
                        rejouer = True
                    elif input_rejouer == "n":
                        rejouer == False
                        bonChoix == True
                        sys.exit()
                    else :
                        print("entrez 'o' pour oui ou 'n' pour non")

#creationJoueur (self, nbJoueur) ==> instancie les joueurs et initialise l'attribut liste_de_joueur
def creationJoueur (self, nbJoueur):
    for i in range(1, nbJoueur+1) : 
        couple = checkNomArgent(i)
        self.liste_de_joueur.append(Joueur(couple[0], couple[1]))


"""
checkNomArgent(nbJoueur) --> (nom_joueur, argent) 
    ==> verifie la fiabilité des inputs (appellé par creationJoueur)
"""  
def checkNomArgent (i):
    ok = False
    nom1 = input("nom du joueur "+str(i)+" : ")

    if nom1 == "quit":
        sys.exit()
        
    while ok == False :
        argent1 = input("De quelle somme dispose "+ nom1+" : ")
        if argent1 == "quit":
            sys.exit()
        try :
            argent1 = int(argent1)
            if argent1<1:
                print("Merci d'entrer un nombre superieur à 0")
            else :
                ok = True
        except :
            print("Merci d'entrer un nombre superieur à 0")
            if argent1 == "quit":
                sys.exit()          
    
    return (nom1, argent1)
 
"""
checkScore(liste_de_joueur) 
    ==> mets a jour les statuts des joueurs si blackjack ou si >21
"""           
            
def checkScore(listeJoueur):
    for joueur in listeJoueur:
        if joueur.valeurMain == 21 :
            joueur.statut = "blackJack"
            print(joueur.nom + " fait un BLACKJACK")
        elif  joueur.valeurMain > 21 :
            joueur.statut = "perdu"


"""
checkEndGame (liste_de_joueur, croupier) --> True si la partie est fini sinon False 
==> met a jour les statuts joueurs ("stop" s'il ne veulent plus tirer de carte sinon "encore")
==> si tous les joueurs ne sont plus à "encore" => la partie est finie
                                                => tirage final de cartes pour le croupier si < 18
                                                => affichage des cartes et score du croupier
                                                => affichage des scores des joueurs et de leur gain
                                                => mise à jour de l'argent des joueurs
                                                => maj joueur.statut = "encore"
"""            
def checkEndGame(listeJoueur, croupier):
    compteur = 0
    for joueur in listeJoueur:
        if joueur.statut != "encore":
            compteur += 1
    
    if compteur == len(listeJoueur):
        print("\n\nla partie est finie !")
        
        while croupier.valeurMain < 17 :                
            croupier.tirer_1_carte(croupier, croupier.jeu)
        time.sleep(2)
        print("le croupier a pour carte : " +str(croupier.main))
        print("le croupier a pour score : "+str(croupier.valeurMain) +"\n")
            
        if croupier.valeurMain > 21 :
            croupier.valeurMain = -1
        
        
        for joueur in listeJoueur:
            time.sleep(2)
            print(joueur.nom + " a pour score " + str(joueur.valeurMain))
            if joueur.valeurMain > croupier.valeurMain and joueur.valeurMain < 22:
                print(joueur.nom + " a gagné " + str(joueur.mise * 2) +"\n")
                joueur.setArgent(joueur.mise * 2)
                print(joueur.nom + " à maintenant "+ str(joueur.argent))
            elif joueur.valeurMain == croupier.valeurMain and joueur.valeurMain < 22:
                print("égalité : " + joueur.nom + " récupere sa mise il dispose maintenant de "+ str(joueur.argent)+ "\n")
                joueur.setArgent(joueur.mise)
            else :
                print(joueur.nom + " a perdu ! Il lui reste : "+ str(joueur.argent) +"\n")
        
        reinitialisationStatut(listeJoueur)
        return True
    else :
        return False

"""
miser(liste_de_joueur)
    => verifie l'input
    => verifie que le joueur possede assez d'argent / mise
"""
def miser(liste_de_joueur):
    for joueur in liste_de_joueur:
        bonChoix = False
        while bonChoix == False:
            if str(type(joueur)) != "<class 'Croupier.Croupier'>":
                
                #print("Dans miser() joueur.mise = " + str(joueur.mise) + " joueur.argent = "+ str(joueur.argent))
                try : 
                    
                    mise = int(input( joueur.nom +" combien voulez vous miser pour cette partie ? "))
                    if mise <= joueur.argent:
                        #print("dans mon if")
                        joueur.setMise(mise)
                        joueur.setArgent(-mise)
                        #print(str(joueur.argent))
                        bonChoix = True
                    else :
                        print("mise > argent possedé... essaye encore ! il vous reste : " + str(joueur.argent))
                except :
                    print("je n'ai pas compris votre mise")



"""
removeJoueur(partie, liste_de_joueur)
    => verifie que les joueurs ont encore de l'argent avant de recommencer une partie
"""       
def removeJoueur (liste_de_joueur):
    for joueur in liste_de_joueur:
        print(joueur.nom)
        if joueur.argent <= 0 :
            liste_de_joueur.remove(joueur)
            print("le joueur : " + joueur.nom + " quitte la table il n'a plus d'argent...")
    if liste_de_joueur == [] : 
        print("il n'y a plus de joueur... Le casino ferme ses portes\n\n\n")
        time.sleep(3)
        sys.exit()

# reinitialise les joueur.statut a "encore" avant de reprendre une partie
def reinitialisationStatut(liste_de_joueur):
    for joueur in liste_de_joueur:
        joueur.statut = "encore"
          