import time
from datetime import datetime, timedelta
from threading import Event, Thread

# Variable globale pour l'heure définie
set_time = None

def display_time(mode=True):
    """Affiche l'heure actuelle ou l'heure définie manuellement dans le mode sélectionné."""
    global set_time
    try:
        while True:
            # Utiliser l'heure définie manuellement si disponible, sinon utiliser l'heure actuelle
            if set_time:
                current_time = set_time
                set_time += timedelta(seconds=1)  # Incrémenter l'heure définie d'une seconde
            else:
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

def set_time_function(hours, minutes, seconds):
    """Permet de définir une heure personnalisée."""
    global set_time  # Déclare que cette variable est globale
    current_time = datetime.now()
    # Mettre à jour l'heure avec les valeurs spécifiées
    set_time = current_time.replace(hour=hours, minute=minutes, second=seconds)
    print(f"\nHeure définie à {set_time.strftime('%H:%M:%S')}.\n")  # Ajouter un retour à la ligne

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

    # Lancer l'affichage de l'heure dans un thread séparé
    time_thread = Thread(target=display_time, args=(mode,))
    time_thread.daemon = True  # Le thread se termine lorsque le programme principal se termine
    time_thread.start()

    # 2. Demander si l'utilisateur veut régler l'heure
    adjustment = input("\nVoulez-vous définir l'heure ? (oui/non) : ").strip().lower()
    if adjustment == "oui":
        heures = int(input("Entrez les heures (0-23) : "))
        minutes = int(input("Entrez les minutes (0-59) : "))
        secondes = int(input("Entrez les secondes (0-59) : "))
        set_time_function(heures, minutes, secondes)
    else:
        print(f"Heure actuelle : {datetime.now().strftime('%H:%M:%S')}\n")

    # Garder le programme actif pour afficher l'heure
    while True:
        time.sleep(1)

# Appeler la fonction principale
main()
