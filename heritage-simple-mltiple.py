"""
0.2.2 Heritage simple et multiple
 De nir une classe Mammifere, qui contiendra un ensemble de caracteristiques propres a ce
 type danimal (nom, age, nombre de dents ...).
 A partir de cette classe, nous pourrons alors deriver une classe Primate, une classe
 Rongeur, et une classe Carnivore, qui heriteront toutes les caracteristiques de la classe
 Mammifere, en y ajoutant leurs speci cites.
 Au depart de la classe Carnivore, deriver une classe Belette, une classe Loup et une
 classe Chien, qui heriteront encore une fois toutes les caracteristiques de la classe parente
 avant dy ajouter les leurs.
 De nir une classe Herbivore derive de la classe Primate
 De nir une classe Omnivore, qui herite de la classe Carnivore et de la classe Herbivore
 """
class Mammifere:
     def __init__(self,nom="daniel",age=20,nombre_de_dents=20):
         self.nom=nom
         self.age=age
         self.nb_dents=nombre_de_dents
         
     def se_nourrir(self):
        return f"{self.nom} mange la viande"
class Primate(Mammifere):
    def __init__(self, nom, age, nombre_de_dents,couleur):
        super().__init__(nom, age, nombre_de_dents)
        
        self.couleur=couleur
        
    def se_nourrir(self):
        return f"{self.nom} mange la chaire"
        
class Rongeur(Mammifere):
    def __init__(self, nom, age, nombre_de_dents,poilu):
        super().__init__(nom, age, nombre_de_dents)
        self.poilu=poilu

class Carnivoire(Mammifere):
    def __init__(self, nom, age, nombre_de_dents,vitesse):
        super().__init__(nom, age, nombre_de_dents)
        self.vitesse=vitesse
    
    
    
class Balette(Carnivoire):
    def __init__(self, nom, age, nombre_de_dents, vitesse,taille):
        super().__init__(nom, age, nombre_de_dents, vitesse)
        self.taille=taille
        
class Loup(Carnivoire):
    def __init__(self, nom, age, nombre_de_dents, vitesse):
        super().__init__(nom, age, nombre_de_dents, vitesse)

    
    
class Chien(Carnivoire):
    def __init__(self, nom, age, nombre_de_dents, vitesse):
        super().__init__(nom, age, nombre_de_dents, vitesse)
    
    

class Herbivore(Primate):
    def __init__(self, nom, age, nombre_de_dents, couleur):
        super().__init__(nom, age, nombre_de_dents, couleur)
        self.couleur=couleur

class Omnivore(Carnivoire,Herbivore):
    def __init__(self, nom, age, nombre_de_dents, vitesse):
        super().__init__(nom, age, nombre_de_dents, vitesse)

homme=Mammifere(nom="daniel",age=25,nombre_de_dents=32)
print(homme.se_nourrir())

