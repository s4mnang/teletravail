1. pour faire l'environnement virtuel et compiler:
py -3 -m venv .venv
. .\.venv\Scripts\Activate

2. Installation (Windows)

Ouvre un terminal PowerShell dans le dossier du script et exécute :

pip install pyautogui pyinstaller

3. Création de l’exécutable

Toujours dans le même dossier :

pyinstaller --onefile mouse_looper.py


Cela crée un exécutable ici :

dist/mouse_looper.exe


si vous avez des questions, demandez a une IA :)