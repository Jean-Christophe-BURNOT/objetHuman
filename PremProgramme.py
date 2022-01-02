# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:13:05 2020

@author: Burnot Jean-Christop
"""
sep = "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
class Humain:
    """
    Classe des êtres humains
    """
    #créer l'attribut de classe qui va s'appliquer à tous les objets
    humain_crees = 0
    
    def __init__(self, c_prenom, c_age):
        print(sep)
        print("Création d'un humain")
        
        #Ici on va créer des attributs (prenom et age qui seront liés a l'objet créer par la classe)
        self.prenom = c_prenom
        self.age = c_age
        #modifie l'attribut de classe
        Humain.humain_crees += 1
        
        
        
        
        
        
print("lancement du programme")
print(sep)
h1 = Humain("Thomas", 34)
#On peut modifier l'attribut de notre objet par la ligne suivante:
h1.prenom = "Jojo"
#On va afficher l'attribut prénom lié à l'objet h1 créer par la classe Humain
print("Prénom de h1: {}".format(h1.prenom))
print("Âge de h1: {}".format(h1.age))
#l'attribut humain_crees va s'utiliser sur la classe et non sur un objet c'est un attribut de classe
print("humain existants: {}".format(Humain.humain_crees))

h2 = Humain("Albert", 17)
#On va afficher l'attribut prénom lié à l'objet h2 créer par la classe Humain
print("Prénom de h2: {}".format(h2.prenom))
print("Âge de h2: {}".format(h2.age))
#l'attribut humain_crees va s'utiliser sur la classe et non sur un objet c'est un attribut de classe

print("humain existants: {}".format(Humain.humain_crees))

