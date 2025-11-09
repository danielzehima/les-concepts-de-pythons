class Article:
    #definir le constructeur
    def __init__(self,numero:int,prixHT:float,designetion,quantite:int,devise="£"):
        self.numero_article=numero
        self.nom_article=designetion
        self.prix_ht_article=prixHT
        self.la_quantite=quantite
        self.devise=devise
    
    def calculer_prixttc(self):
        resultat=float(self.prix_ht_article*self.la_quantite+self.prix_transport())
        return resultat  
    def prix_transport(self):
        rest=float(self.prix_ht_article*5/100)
        return rest
    
    def retirer_article(self,nbre):
        self.la_quantite-=nbre
        return self.la_quantite
    
    def ajouter_article(self,nbre):
        self.la_quantite+=nbre
        return self.la_quantite

    def __str__(self):
        return f" {self.numero_article}-{self.nom_article} coute {self.prix_ht_article} {self.devise} - En stock : {self.la_quantite}"
# implementation

article1=Article(1,12,"banane",5,devise="$")
article2=Article(2,20,"Oranges",10,devise="$")
article1.ajouter_article(5)
article1.retirer_article(2)
print(article1)
print(article2)
print("Frais de transport article 1:\n",article1.prix_transport(),"$")
print("Frais de transport artile 2 :\n",article2.prix_transport(),"$")

print("article 1 : ",article1.calculer_prixttc(),"$")