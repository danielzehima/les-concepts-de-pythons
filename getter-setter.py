class Produit:
    def __init__(self,nom,prix):
        self._prix=prix
        self.nom=nom
    @property
    def prix(self):
        
        return self._prix
    
    @prix.setter
    def prix(self,nouveau_prix):
        
        if nouveau_prix>0:
            self._prix=nouveau_prix
            return self._prix
        else:
            raise ValueError("Le prix ne doir pas être négatif")
       
            
prod=Produit("Smarphone",150)
print("prix initial :",prod.prix)

prod.prix=200
print("nouveau prix : ",prod.prix)

try:
    prod.prix=-200
except ValueError as e:
    print("Erreur cotchée ",{e})

print(f"prix après tentative échouée : {prod.prix}")