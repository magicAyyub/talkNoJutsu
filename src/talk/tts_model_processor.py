from pathlib import Path
from src.settings import *
import subprocess
import os
import stat
from colorama import Fore, Style

class TTSModelProcessor:
    def __init__(self, bash_script=BASE_DIR / '/src/operation/tts_lists_process.sh'):
        self.bash_script = bash_script

    def make_executable(self):
        # Vérifier si le fichier existe avant de tenter de modifier ses permissions
        if os.path.isfile(self.bash_script):
            # Ajouter la permission d'exécution pour l'utilisateur
            os.chmod(self.bash_script, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
            print(f"{Fore.GREEN}Le script {self.bash_script} est maintenant exécutable.{Style.RESET_ALL}")
        else:
            raise FileNotFoundError(f"Le script {self.bash_script} n'a pas été trouvé.")

    def generate_list(self):
        try:
            # Vérifier si le script bash est exécutable, sinon le rendre exécutable
            if not os.access(self.bash_script, os.X_OK):
                print(f"{Fore.YELLOW}Le script {self.bash_script} n'est pas exécutable. Tentative de modification des permissions...{Style.RESET_ALL}")
                self.make_executable()
            
            # Exécuter le script bash
            subprocess.run(['bash', self.bash_script], check=True)
            print(Fore.GREEN + "Le traitement des modèles est terminé et les données ont été enregistrées." + Style.RESET_ALL)

        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Une erreur s'est produite lors de l'exécution du script : {e}{Style.RESET_ALL}")
        except FileNotFoundError as e:
            print(f"{Fore.RED}Fichier non trouvé : {e}{Style.RESET_ALL}")
        except PermissionError as e:
            print(f"{Fore.RED}Erreur de permission : {e}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}Une erreur inattendue est survenue : {e}{Style.RESET_ALL}")
