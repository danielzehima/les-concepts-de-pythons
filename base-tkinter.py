import tkinter as tk
import customtkinter as ctk
import requests
#creer une fenêtre
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")



root=ctk.CTk()
root.geometry("600x350")
root.title("Convertisseur de devises")

URL_TAUX_API = "https://api.exchangerate.host/latest?base=USD&symbols=EUR"

def recuperer_taux():
    """Récupère le taux USD vers EUR actuel via l'API."""
    try:
        response = requests.get(URL_TAUX_API)
        response.raise_for_status()  # Lève une erreur si la requête échoue (4xx ou 5xx)
        
        data = response.json()
        
        # 💥 Le taux est stocké dans la structure data['rates']['EUR']
        taux = data['rates']['EUR']
        return taux
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau/API: {e}")
        # En cas d'échec de l'API, nous retournons un taux par défaut ou levons une erreur
        return None

import tkinter as tk
import customtkinter as ctk
import requests # 💥 Importation du module requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root=ctk.CTk()
root.geometry("600x350")
root.title("Convertisseur de devises")

# --- URL de l'API de Taux de Change ---
# Conversion de USD vers EUR
URL_TAUX_API ="https://cdn.taux.live/api/latest.json"
params = {
    "base": "USD",
    "rates": {
        "AED": 3.67297,
        "AFN": 89.647021,
        "ALL": 104.709024,
        "AMD": 476.665393,
        "ANG": 1.789593,
        "AOA": 597.455,
        "ARS": 99.2347,
        "AUD": 1.338279,
    },
}

#Source: https://taux.live/pages/api


def recuperer_taux():
    """Récupère le taux USD vers EUR actuel via l'API."""
    try:
        response = requests.get(URL_TAUX_API, params=params)
        response.raise_for_status() 
        
        data = response.json()
        
        # 💥 CORRECTION MAJEURE ICI 💥
        # Vérifier si l'API indique que l'opération a réussi
        if 'success' in data and data['success'] == True:
            # Si le succès est confirmé, nous continuons à chercher le taux
            taux = data['rates']['USD']
            return taux
        else:
            # Si 'success' est False ou manquant (ou si une autre erreur est présente)
            print("Erreur API: La réponse JSON n'indique pas un succès.")
            if 'error' in data:
                 # Si l'API renvoie un message d'erreur explicite
                 print(f"Message d'erreur de l'API : {data['error']['info']}")
            return None # Retourne None pour indiquer l'échec

    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau/API (connexion, timeout, etc.): {e}")
        return None


def convertir():
    """Effectue la conversion en utilisant le taux réel de l'API."""
    try:
        # 1. Tenter la conversion du texte en nombre (gestion de ValueError)
        montant_saisi = float(ma_saisie.get())
        
        # 2. Récupérer le taux réel
        taux_reel = recuperer_taux()
        
        if taux_reel is None:
            label_convertir.configure(text="Erreur : API non disponible.", text_color="red")
            return
            
        # 3. Calculer le montant total
        montant_total = montant_saisi * taux_reel
        
        # 4. Afficher le résultat
        label_convertir.configure(text=f"{montant_total:.2f} EUR", text_color="#2ecc71") # Vert pour succès
        
    except ValueError:
        # Si la saisie n'est pas un nombre
        label_convertir.configure(text="Erreur : Entrez un montant valide.", text_color="red")
    except Exception as e:
        label_convertir.configure(text=f"Erreur inattendue.", text_color="red")
        print(f"Erreur : {e}")


# --- 3. Configuration des Widgets (Le reste de ton code) ---
# NOTE: J'ai juste ajouté quelques couleurs pour mieux visualiser les statuts

monlabel = ctk.CTkLabel(root, text="Montant : ", font=("Times new roman", 14, "bold"))
monlabel.grid(row=0, column=0, padx=10, pady=20)

ma_saisie = ctk.CTkEntry(root, font=("Arial", 20), width=150)
ma_saisie.grid(row=0, column=1, pady=20)
 
btn = ctk.CTkButton(root, text="Convertir", cursor="hand2", font=("Arial", 15), command=convertir)
btn.grid(row=2, column=1, pady=20)

label_convertir = ctk.CTkLabel(root, text="Résultat : 0.00", width=150, font=("Arial", 20))
label_convertir.grid(row=1, column=1, pady=20)

label_usd = ctk.CTkLabel(root, text="De USD", width=150, font=("Arial", 13))
label_usd.grid(row=0, column=2, pady=20)

label_euro = ctk.CTkLabel(root, text="Vers Euro : ", width=150, font=("Arial", 13))
label_euro.grid(row=1, column=0, pady=20)


root.mainloop()