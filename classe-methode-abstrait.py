from abc import ABC,abstractmethod

class TableauTrieAbstrait(ABC):
    def __init__(self):
        self._tableau=[]
        
    @abstractmethod
    def plusGrand(self,a,b)->bool:
        pass
    
    def inserer(self,element):
        if not self._tableau:
            self._tableau.append(element)
            return 
        for i, existant  in enumerate(self._tableau):
            
            if not self.plusGrand(element,existant):
                self._tableau.insert(i,element)
                return
        self._tableau.append(element)
        
    def afficher_tableau(self):
        print(f"Tableau : {self._tableau}")
        
               
class TrieEntier(TableauTrieAbstrait):
    
    def plusGrand(self, a:int, b:int):
       return a>b

class TableauChaines(TableauTrieAbstrait):
    def plusGrand(self, a:str, b:str):
      return len(a)>len(b)
  
#test
gestionnaire_entier=TrieEntier()


gestionnaire_entier.inserer(10)

gestionnaire_entier.inserer(6)

gestionnaire_entier.inserer(8)

gestionnaire_entier.inserer(12)

gestionnaire_entier.inserer(3)


gestionnaire_entier.afficher_tableau()

print("\nTableau des chaines triés par longueur")
gestionnaire_chaines=TableauChaines()
gestionnaire_chaines.afficher_tableau()

gestionnaire_chaines.inserer("tableau")
gestionnaire_chaines.inserer("alfred")
gestionnaire_chaines.inserer("presidence")
gestionnaire_chaines.inserer("python")
gestionnaire_chaines.inserer("langage c#")
gestionnaire_chaines.inserer("langage c++")

gestionnaire_chaines.afficher_tableau()
