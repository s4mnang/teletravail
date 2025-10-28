import pyautogui
import time
import sys

pyautogui.FAILSAFE = False  # pas d’arrêt si on touche un coin

def move_left_right(pixels=100, duration=15):
    # position de départ
    x0, y0 = pyautogui.position()
    end_time = time.time() + duration
    while time.time() < end_time:
        # va à gauche
        pyautogui.moveTo(x0 - pixels, y0, duration=0.3)
        # puis à droite
        pyautogui.moveTo(x0 + pixels, y0, duration=0.3)
        # revient au centre
        pyautogui.moveTo(x0, y0, duration=0.3)

def main():
    print("Attente 15 s avant démarrage...")
    time.sleep(15)
    print("Boucle active. Ferme la fenêtre pour arrêter.")
    while True:
        move_left_right(pixels=100, duration=15)  # 10 cm ≈ 100 px sur un écran classique
        print("Pause 30 s...")
        time.sleep(30)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nArrêt manuel.")
        sys.exit(0)
