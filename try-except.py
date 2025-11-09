
   
def calcler_impots(revenu):
    if revenu<0:
        raise ValueError("le revenu ne peut pas être négatif")
    else:
        print("Calcul des impôts  est en cours....")

def division(a,b):
    
    if b==0:
        raise ZeroDivisionError("Division par zero, impossibel!")
    else:
       resultat=a/b
       print(f"la divison de {a} par {b} est {resultat:.2f}")
       return resultat

try:
    division(10,9)
except ZeroDivisionError as e:
    print(f"Erreur lors de la division : {e}")

try:
    division(10,0)
except ZeroDivisionError as e:
    print(f"Erreur lors de la division : {e}")