"""
 Exercice supplementaire 8.2. Classe Time
 Definir une nouvelle classe Time, qui nous permettra de d'effectuer toute une serie doperations
 sur des instants, des durees, etc.
 Ajouter les attributs pays, heure, minute et seconde.
 Creer un objet instant qui contient une date particuliere.
 Ecrivez une fonction affiche
 heure() qui permet de visualiser le contenu dun objet de
 classe Time sous la forme conventionnelle heure :minute :seconde .
 Appliquee a lobjet instant la fonction affiche
 heure()
 Encapsuler la fonction affiche
 heure() dans la classe Time (methode affiche)
 Instancier un objet maintenant
 Tester la methode
 ! Unefonction qui est ainsi encapsulee dans une classe sappelle une methode_
"""
import time


class Time:
    def __init__(self,pays="local",heure=0,minute=0,seconde=0):
        self.pays=pays
        self.heure=heure
        self.minute=minute
        self.seconde=seconde
        
    def affiche_heure(self):
        
        heure_formatee=str(self.heure).zfill(2)
        minute_formatee=str(self.minute).zfill(2)
        seconde_formatee=str(self.seconde).zfill(2)
        
        print(f"{self.pays} {heure_formatee}:{minute_formatee}:{seconde_formatee}")

instant=Time("Cote d'ivoire",20,30,15)
instant.affiche_heure()
maintenant=Time()
maintenant = Time(pays="Tokyo", heure=23, minute=59, seconde=59)
maintenant.affiche_heure()

