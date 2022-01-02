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
    lieu_habitation = "Terre1"
    
    def __init__(self, c_prenom, c_age):
        print(sep)
        print("Création d'un humain")
        
        #Ici on va créer des attributs (prenom et age qui seront liés a l'objet créer par la classe)
        self.prenom = c_prenom
        self.age = c_age
        #modifie l'attribut de classe
        Humain.humain_crees += 1
        
        
        
        #définit la méthode d'objet "parler" qui permet
        #au objets crées par humain de parler
    def parler(self, message):
        print("{} a dit : {}".format(self.prenom, message))
        return message
    
        #Définit une méthode de classe changer dimension
        #on doit mettre cls... cls=méthode de classe
    def changer_dimension(cls, modif):
        Humain.lieu_habitation = modif
        
    #ligne nécéssaire qui permet de dire que changer dimension est une
    #méthode de classe le nom qu'on devra utiliser pour appeller cette
    #méthode de classe est le nom à gauche du égal
    changer_dimension=classmethod(changer_dimension)
    
    #Définit une méthode statique
    def definition():
        print("Humain: Robot doté de conscience qui finira par faire la guerre")
    definition = staticmethod(definition)
         
        
        
"""
Programme principal
"""
        
Humain.definition()
print(sep)

"""
séance 1
"""
  
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

"""
Séance 2
"""

print("humain existants: {}".format(Humain.humain_crees))
print(sep)
print(sep)
test = h1.parler("AEIOUY")
print(test)
print("test validé")
h1.parler("Bonjour à tous !")
h2.parler("Bonjour semblable")
print("planète actuelle : {}".format(Humain.lieu_habitation))
Humain.changer_dimension("Terre616")
print("nouvelle planète actuelle : {}".format(Humain.lieu_habitation))
print(sep)


