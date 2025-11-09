class Employe:
    def __init__(self,nom,salaire):
        self.nom=nom
        self.salire=salaire
    
    def se_presenter(self):
        print(f"Je suis {self.nom} , je gagne {self.salire} dollars comme salaire")
        print("Mon rôle est de faire mon travail général")
    
    def travailler(self):
        print(f"{self.nom} est en train de gérer ses tâches quotidiennes")

class Developpeur(Employe):
    def __init__(self, nom, salaire,langage_prefere):
        super().__init__(nom, salaire)
        self.langage_prefere=langage_prefere
    
    def coder(self):
        print(f"{self.nom} est en train de coder en {self.langage_prefere}")

    def travailler(self):
        print(f"{self.nom} est en train de coder en python . ")
        
class Manager(Employe):
    def __init__(self, nom, salaire,nbre_equipe_geree):
        super().__init__(nom, salaire)
        self.equipe_geree=nbre_equipe_geree
    
    def organiser_reunion(self):
        print(f"je suis {self.nom}, j'origanise des réunions avec une equipe de {self.equipe_geree} personnes ")

    def travailler(self):
        print(f"{self.nom} est en train de coordonner ses équipes . ")

class Comptable(Employe):
    
    def travailler(self):
        print(f"{self.nom}, le comptable est en train de gérer sa comptabilité . ")
    
manager1=Manager(nom="Daniel",salaire=15000,nbre_equipe_geree=15)
develop1=Developpeur(nom='alphonse',salaire=5000,langage_prefere="Python")
comptable1=Comptable(nom="Felix",salaire=1000)

employes=[comptable1,manager1,develop1]

for employe in employes:
    employe.travailler()