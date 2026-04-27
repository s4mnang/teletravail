import pyautogui
import time
import random
import math
import sys
import threading
import tkinter as tk
from datetime import datetime

pyautogui.FAILSAFE = True

stop_event = threading.Event()


def log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")


def move_circle():
    screen_w, screen_h = pyautogui.size()
    cx, cy = screen_w // 2, screen_h // 2

    radius = random.randint(180, 480)
    steps = random.randint(90, 240)
    speed = random.uniform(0.005, 0.02)

    for i in range(steps):
        if stop_event.is_set():
            return
        angle = 2 * math.pi * i / steps
        x = int(cx + radius * math.cos(angle))
        y = int(cy + radius * math.sin(angle))
        pyautogui.moveTo(x, y, duration=speed)
        time.sleep(random.randint(1, 10) / 1000)


def recenter():
    screen_w, screen_h = pyautogui.size()
    pyautogui.moveTo(screen_w // 2, screen_h // 2, duration=0.3)


def stop_button_window():
    root = tk.Tk()
    root.title("Anti-AFK")
    root.resizable(False, False)
    root.attributes("-topmost", True)

    # Keep window on top-right so it's easy to find
    root.geometry("160x60+{}+0".format(root.winfo_screenwidth() - 170))

    def on_stop():
        stop_event.set()
        root.destroy()

    btn = tk.Button(root, text="Arrêter", command=on_stop,
                    bg="#c0392b", fg="white", font=("Arial", 12, "bold"),
                    relief="flat", padx=10, pady=6)
    btn.pack(expand=True, fill="both", padx=6, pady=6)

    # Also allow closing the window directly
    root.protocol("WM_DELETE_WINDOW", on_stop)
    root.mainloop()


def main():
    # Start the stop-button window in a daemon thread
    ui_thread = threading.Thread(target=stop_button_window, daemon=True)
    ui_thread.start()

    log("Démarrage dans 15 secondes...")
    for _ in range(15):
        if stop_event.is_set():
            break
        time.sleep(1)

    log("Boucle active. Cliquez sur 'Arrêter' ou Ctrl+C pour stopper.")

    iterations_until_click = random.randint(2, 5)
    loop_count = 0

    while not stop_event.is_set():
        loop_count += 1
        do_click = loop_count >= iterations_until_click

        move_circle()
        if stop_event.is_set():
            break

        if do_click:
            pyautogui.click(1, 1)
            loop_count = 0
            iterations_until_click = random.randint(2, 5)
            action = "move+click"
        else:
            action = "move"

        recenter()

        sleep_secs = random.uniform(60, 100)
        log(f"Action: {action} | Prochain cycle dans {sleep_secs:.0f}s")

        # Sleep in small increments so stop_event is checked often
        deadline = time.time() + sleep_secs
        while time.time() < deadline and not stop_event.is_set():
            time.sleep(1)

    log("Arrêté.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_event.set()
        print("\nAu revoir !")
        sys.exit(0)
