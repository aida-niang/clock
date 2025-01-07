import time
from datetime import datetime

def display_time(mode=True):
    """Affiche l'heure selon le mode 12h ou 24h."""
    try:
        while True:
            current_time = datetime.now()

            # Formater l'heure selon le mode sélectionné
            if mode:
                formatted_time = current_time.strftime("%H:%M:%S")  # Format 24 heures
            else:
                formatted_time = current_time.strftime("%I:%M:%S %p")  # Format 12 heures avec AM/PM

            # Afficher l'heure dans la même ligne
            print(f"\r{formatted_time}", end="")

            # Attendre une seconde avant de mettre à jour l'heure
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgramme arrêté.")

def select_mode():
    """Permet à l'utilisateur de choisir le mode d'affichage de l'heure."""
    while True:
        choice = input("Choisissez le mode d'affichage (12h ou 24h) : ").strip().lower()  # Convertir la saisie en minuscules
        if choice == "12h":
            return False  # Mode 12 heures
        elif choice == "24h":
            return True  # Mode 24 heures
        else:
            print("❌ Choix invalide. Veuillez entrer '12h' ou '24h'.")

def main():
    # 1. Demander le mode d'affichage
    print("Bienvenue dans le programme d'affichage de l'heure.\n")
    mode = select_mode()  # Demander à l'utilisateur de choisir le mode d'affichage

    # 2. Lancer l'affichage de l'heure en fonction du mode sélectionné
    display_time(mode)

# Appeler la fonction principale
main()
