"""
10.2.1 Exercices preparatoires
 Gestion dheures complementaires Chaque enseignant de luniversite e ectue un certain
 nombre dheures denseignement dans une annee. Suivant le statut de lenseignant, un certain
 nombre de ces heures peut-etre considere comme complementaire. Les heures complementaires
 sont payees separement a lenseignant. Les volumes horaires sont exprimes en heures entieres et
 le prix dune heure complementaire est de 10 Euros.
 Le nom et le nombre dheures total dun enseignant sont fixes a sa creation, puis seul le nom
 peut etre librement consulte (methode nom()).
 Dautre part on veut pouvoir librement consulter un enseignant sur son volume dheures comple
mentaires (methode hc()) et sur la retribution correspondante (methode retribution()).
 Il y a deux types denseignants :
 les intervenants exterieurs : toutes les heures effectuees sont complementaires,
 les enseignants de la fac : seules les heures assurees au dela dune charge statutaire de 192h
 sont complementaires.
 Questions :
 1. Sans ecrire de code, modeliser les enseignants : quelles sont les classes? ou sont implementees
 les methodes? lesquelles sont nouvelles, redefinies
"""
PRIX_HC=10
CHARGE_STATUAIRE=192

class Enseignant:
    def __init__(self,nom,heure_totales):
        self.nom=nom
        self._heure_totales=heure_totales
    
    def get_nom(self):
        return self.nom
    
    def get_hc(self):
        return 0
    
    def retribution(self):
        return self.get_hc()*PRIX_HC

class Enseignant_ext(Enseignant):
    def __init__(self, nom, heure_totales):
        super().__init__(nom, heure_totales)
    
    def hc(self):
        return self._heure_totales
    
class Enseignant_fac(Enseignant):   
    def hc(self):
        heures_complementaire=self._heure_totales-CHARGE_STATUAIRE
        return max(0, heures_complementaire)
    

# ----------------------------------------------------------------------
## 3. Tests

print("--- Test des Intervenants Extérieurs ---")
intervenant1 = Enseignant_ext("Dr. Smith",heure_totales=50)
print(f"Nom: {intervenant1.get_nom()}")
print(f"Heures Totales: {intervenant1._heure_totales}h")
print(f"Heures Complémentaires (hc()): {intervenant1.get_hc()}h")
print(f"Rétribution: {intervenant1.retribution()} Euros\n") # 50 * 10 = 500

print("--- Test des Enseignants de la Faculté ---")
# Cas 1: Moins de 192h
fac1 =Enseignant_fac("Prof. Dupont", 150)
print(f"Nom: {fac1.get_nom()}")
print(f"Heures Totales: {fac1._heure_totales}h")
print(f"Heures Complémentaires (hc()): {fac1.hc()}h") # 150 - 192 = < 0, donc 0
print(f"Rétribution: {fac1.retribution()} Euros\n") # 0 * 10 = 0

# Cas 2: Plus de 192h
fac2 = Enseignant_fac("Dr. Dubois", 250)
print(f"Nom: {fac2.get_nom()}")
print(f"Heures Totales: {fac2._heure_totales}h")
print(f"Heures Complémentaires (hc()): {fac2.hc()}h") # 250 - 192 = 58
print(f"Rétribution: {fac2.retribution()} Euros") # 58 * 10 = 580
     