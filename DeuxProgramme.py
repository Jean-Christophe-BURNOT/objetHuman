# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:05:04 2020

@author: titof
Ce Programme est la partie 3 du cour sur la programmation orientée objet.
Elle portera sur l'encaplsulation.
"""
class Humain:
    def __int__(self, nom, age):
        print("création d'un humain")
        self.nom = nom
        self._age = age
        
        
    def _getage(self):
        print("récuperation interdite")
    """
    #property est une méthode qui permet de créer l'encapsulation
    (bloque l'accès de l'attribut en dehors de la classe)
    """
    age = property(_getage)
    
#Programme principal
h3 = Humain("Jason",26)
print(h3._age)

