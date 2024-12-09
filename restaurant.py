import csv

# Fonction pour lire le menu depuis le fichier CSV
def lire_menu():
    menu = {}
    with open('csv/menu.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu[row['Plat']] = float(row['Prix'])
    return menu

# Initialiser le menu depuis le fichier CSV
menu = lire_menu()

# Que fait cette fonction ? Décrire son utilite et son fonctionnement.
def afficher_menu():
    print("\n--- Menu du Restaurant ---")
    for plat, prix in menu.items():
        print(f"{plat}: {prix:.2f}€")

# Que fait cette fonction ? Décrire son utilite et son fonctionnement.
def prendre_commande():
    commandes = []  # Que déclare t-on ici ?
    while True:
        plat = input("Entrez le nom d'un plat (ou 'fin' pour terminer) : ").capitalize()
        # Décrire ici le fonctionnement des tests suivants :
        if plat == "Fin":
            break
        elif plat in menu:
            commandes.append((plat, menu[plat]))  # Que se passe t-il ici ? Quelle forme cela prend ?
            print(f"{plat} ajouté à la commande.")
        else:
            print("Ce plat n'est pas au menu. Veuillez réessayer.")
    return commandes

# Que fait cette fonction ? Décrire son utilite et son fonctionnement.
def calculer_facture(commandes):
    total = sum(prix for _, prix in commandes)  # Expliquer cette ligne
    print("\n--- Facture ---")
    for plat, prix in commandes:                # Expliquer cette structure de code
        print(f"{plat}: {prix:.2f}€")
    print(f"Total: {total:.2f}€")
    return total

# Programme principal
# Que se passe t-il dans ce bloc de code ?
while True:
    afficher_menu()  # Que se passe t-il ici ?
    commandes = prendre_commande()  # Que se passe t-il ici ?
    if commandes:
        calculer_facture(commandes)  # Que se passe t-il ici ?
    else:
        print("Aucune commande passée.")

    # Que se passe t-il dans ce bloc de code ?
    continuer = input("\nVoulez-vous passer une nouvelle commande ? (oui/non) : ").lower()
    if continuer != "oui":
        print("Merci pour votre visite. À bientôt !")
        break
