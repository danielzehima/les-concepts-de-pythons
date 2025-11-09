from abc import ABC, abstractmethod

class Forme(ABC):
    def __init__(self,nom,unites="cm"):
        self._nom=nom
        self.__unites=unites
    
    @abstractmethod
    
    def calculer_surface(self):
        pass
    
    @abstractmethod
    
    def afficher_proprites(self):
        pass

class Cercle(Forme):
    def __init__(self, nom, rayon, unites="cm"):
        super().__init__(nom, unites)
        self.rayon=rayon
        
    def calculer_surface(self):
        surface=3.14159*self.rayon**2
        return surface
    
    def afficher_proprites(self):
        return f"le {self._nom} a un rayon de {self.rayon}{self._Forme__unites} et une  surface de {self.calculer_surface():.2f}{self._Forme__unites}2 "

class Rectangle(Forme):
    def __init__(self, nom,longueur,largeur, unites="cm"):
        super().__init__(nom, unites)
        self.longueur=longueur
        self.largeur=largeur
    def calculer_surface(self):
        return self.longueur*self.largeur
    
    def afficher_proprites(self):
        return f"le {self._nom} a une longueur de {self.longueur}{self._Forme__unites} et une largeur de {self.largeur}{self._Forme__unites} et sa surface est : {self.calculer_surface()} {self._Forme__unites}2"


#-----tets----
cercle=Cercle("cercle1",5)
rectangle1=Rectangle("Rectangle1",10,5)

cercle.calculer_surface()
rectangle1.calculer_surface()
Liste_forme=[cercle,rectangle1]

for forme in Liste_forme:
    print(forme.afficher_proprites())
        
