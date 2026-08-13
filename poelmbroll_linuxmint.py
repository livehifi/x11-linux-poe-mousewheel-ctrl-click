#!/usr/bin/env python3
import subprocess
import time
from pynput import mouse, keyboard

mouse_controller = mouse.Controller()

ctrl_pressed = False
last_click_time = 0.0
# Minimum time between clicks in seconds (0.035 = 35 ms)
COOLDOWN_DELAY = 0.035

def is_poe_focused():
    """Checks if the active window contains 'Path of Exile' or running via Proton."""
    try:
        active_window = subprocess.check_output(
            ["xdotool", "getactivewindow", "getwindowname"],
            stderr=subprocess.DEVNULL
        ).decode("utf-8", errors="ignore")
        
        window_title = active_window.lower()
        # Matches both native title and Wine/Proton wrappers (e.g., PoE 1 & PoE 2)
        return "path of exile" in window_title or "poe" in window_title
    except Exception:
        return False

def on_press(key):
    global ctrl_pressed
    if key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        ctrl_pressed = True

def on_release(key):
    global ctrl_pressed
    if key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        ctrl_pressed = False

def on_scroll(x, y, dx, dy):
    global last_click_time
    current_time = time.time()

    if dy != 0 and ctrl_pressed and is_poe_focused():
        if (current_time - last_click_time) >= COOLDOWN_DELAY:
            mouse_controller.click(mouse.Button.left, 1)
            last_click_time = current_time

if __name__ == "__main__":
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouse_listener = mouse.Listener(on_scroll=on_scroll)

    keyboard_listener.start()
    mouse_listener.start()

    keyboard_listener.join()
    mouse_listener.join()
