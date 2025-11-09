class Voiture:
    
    #dédfinir le constructeur
    def __init__(self,couleur,marque,vitesse_max):
        self.couleur=couleur
        self.marque=marque
        self.vitesse=vitesse_max
        
    #definir les méthodes
    def klaxonner(self):
        print(f"la {self.marque} klaxonne 'pipiiiii!'")
    

voiture_de_mon_reve=Voiture(couleur="jaune",marque="Range Rover",vitesse_max=350)

print(f"Ma {voiture_de_mon_reve.marque} de couleur {voiture_de_mon_reve.couleur} a une vitesse max de {voiture_de_mon_reve.vitesse}km/h")

voiture_de_mon_reve.klaxonner()