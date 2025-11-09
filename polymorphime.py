"""
 10.2.3 Polymorphisme
 Ecrivez une classe Forme qui contiendra une methode calculAire.
 Faites-en heriter la classes Carre contenant un attribut cote
 idem pour la classe Cercle contenant un attribut rayon.
 Rede nir la methode calculAire pour les classes Carre et Cercle
 De nir une fonction AireTotal qui a partir dun tableau de Forme calcul laire totale
"""
from abc import ABC,abstractclassmethod

class Forme(ABC):
    
    @abstractclassmethod   
    def calculAire(self):
        #raise NotImplementedError("la methode doit être implémenter par les sous-classe")   
        pass
    
  
class Carre(Forme):
    def __init__(self,cote):
        super().__init__()
        self.cote=cote
    
    def calculAire(self):
        return float(self.cote*self.cote)
        
class Cercle(Forme):
    def __init__(self,rayon):
        super().__init__()
        self.rayon=rayon
    def calculAire(self):
        return float((self.rayon**2)*3.14)

def TotalAire(tableau_de_forme):
    
    aire_cumulee=0.0
    
    for forme in tableau_de_forme:
        aire_cumulee+=forme.calculAire()
    return aire_cumulee

aire_carre1=Carre(20)
aire_cercle=Cercle(20)
aire_carre2=Carre(10)
carre1=aire_carre1.calculAire()
carre2=aire_carre2.calculAire()
cercle=aire_cercle.calculAire()

forme_a_calculer=[aire_carre1,aire_cercle,aire_carre2]
aire_total=TotalAire(forme_a_calculer)
print("\n-------Calcul des aires individuelles)------")
print(f"aire du carré (coté 20) est : {carre1:.2f}")
print(f"aire du carré (coté 10) est : {carre2:.2f}")
print(f"aire du cercle (coté 20) est : {cercle:.2f}")
print("\n----Total des aires-----------")
print(f"Total des aires (carré,cercle,carre): {aire_total:.2f}")
