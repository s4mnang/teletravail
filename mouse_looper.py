import pyautogui
import time
import math
import sys

def loop_mouse():
    radius = 300  # rayon du petit cercle
    center_x, center_y = pyautogui.position()
    for angle in range(0, 360, 10):
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        pyautogui.moveTo(x, y, duration=1.0)

def main():
    print("Attente de 15 secondes avant de démarrer...")
    time.sleep(15)
    print("Démarrage de la boucle. Ferme la fenêtre pour arrêter.")
    while True:
        loop_mouse()     # bouge la souris en cercle pendant ~15s
        print("Pause de 30 secondes...")
        time.sleep(30)   # puis attend 30 secondes avant de recommencer

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nArrêt manuel du programme.")
        sys.exit(0)

