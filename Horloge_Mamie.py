import time
from datetime import datetime

def display_time():
    try:
        while True:
            # Obtenir l'heure actuelle
            actual_time = datetime.now()
            
            # Formater l'heure sous la forme hh:mm:ss
            formatted_time = actual_time.strftime("%H:%M:%S")
            
            # Afficher l'heure dans la même ligne (utile pour la mise à jour)
            print(f"\r{formatted_time}", end="")
            
            # Attendre une seconde avant de mettre à jour
            time.sleep(1)

            # Message quand l'utilisateur appuie sur ctrl + c
    except KeyboardInterrupt:
        print("\nProgramme arrêté.")

# Appeler la fonction pour afficher l'heure
display_time()
