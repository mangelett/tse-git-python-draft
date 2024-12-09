import csv

# Fonction pour lire les livres depuis le fichier CSV
def lire_bibliotheque():
    bibliotheque = {}
    with open('csv/bibliotheque.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            bibliotheque[row['Titre']] = row['Auteur']
    return bibliotheque

# Fonction pour écrire les emprunts dans le fichier CSV
def ecrire_emprunts(emprunts):
    with open('csv/emprunts.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Titre', 'Auteur'])
        writer.writerows(emprunts)

# Initialiser la bibliothèque depuis le fichier CSV
bibliotheque = lire_bibliotheque()

# Que fait cette fonction ? Décrire son utilite et son fonctionnement.
def afficher_bibliotheque():
    print("\n--- Bibliothèque ---")
    for titre, auteur in bibliotheque.items():
        print(f"Titre: {titre}, Auteur: {auteur}")

# Que fait cette fonction ? Décrire son utilite et son fonctionnement.
def emprunter_livre():
    emprunts = []  # Que déclare t-on ici ?
    while True:
        titre = input("Entrez le titre d'un livre à emprunter (ou 'fin' pour terminer) : ").title()
        # Décrire ici le fonctionnement des tests suivants :
        if titre == "Fin":
            break
        elif titre in bibliotheque:
            emprunts.append((titre, bibliotheque[titre]))  # Que se passe t-il ici ? Quelle forme cela prend ?
            print(f"{titre} emprunté.")
        else:
            print("Ce livre n'est pas disponible. Veuillez réessayer.")
    ecrire_emprunts(emprunts)
    return emprunts

# Que fait cette fonction ? Décrire son utilite et son fonctionnement.
def afficher_emprunts(emprunts):
    print("\n--- Livres Empruntés ---")
    for titre, auteur in emprunts:                # Expliquer cette structure de code
        print(f"Titre: {titre}, Auteur: {auteur}")
    if not emprunts:
        print("Aucun livre emprunté.")

# Programme principal
# Que se passe t-il dans ce bloc de code ?
while True:
    afficher_bibliotheque()  # Que se passe t-il ici ?
    emprunts = emprunter_livre()  # Que se passe t-il ici ?
    afficher_emprunts(emprunts)  # Que se passe t-il ici ?

    # Que se passe t-il dans ce bloc de code ?
    continuer = input("\nVoulez-vous emprunter un autre livre ? (oui/non) : ").lower()
    if continuer != "oui":
        print("Merci pour votre visite. À bientôt !")
        break
