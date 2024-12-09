# Que déclare t-on ici ?
bibliotheque = {
    "Le Petit Prince": "Antoine de Saint-Exupéry",
    "1984": "George Orwell",
    "Moby Dick": "Herman Melville",
    "L'Étranger": "Albert Camus"
}

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
