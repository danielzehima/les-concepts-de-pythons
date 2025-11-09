from abc import ABC, abstractmethod

class Employe(ABC):
    def __init__(self,nom):
        self.nom=nom
    
    @abstractmethod
    def travailler(self):
        pass
    
    @classmethod
    @abstractmethod
    def creer_employe_de_zero(cls,nom_saisi):
        pass
    
    
    def se_presenter(self):
        print(f"je suis {self.nom} je fais mes obligations quotidiennes . ")

class Commercial(Employe):
    
    def travailler(self):
        print(f"Je suis {self.nom} le commercial, je fait la publicité de tous les produits de la boîte . ")
    
    @classmethod
    def creer_employe_de_zero(cls,nom_saisi):
        print(f"un nouveau commercial {nom_saisi} a été créé par la classe {cls.__name__}")
        return cls(nom_saisi)
    

class Developpeur(Employe):
    
    def travailler(self):
        print(f" Je suis {self.nom} je code avec le langage python")

commercial1=Commercial("bob")
commercial1.travailler()

nouveau_commercial=Commercial.creer_employe_de_zero("Albéric")
nouveau_commercial.travailler()
nouveau_commercial.se_presenter()
