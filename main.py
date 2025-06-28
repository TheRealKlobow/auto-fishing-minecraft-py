import sounddevice as sd
import numpy as np
import pyautogui
import time
import random

threshold = 0.1
cooldown = 1.0
cast_delay = 0.2
delay_after_sound = 0.2
mouse_move_delay = 2  # Time after cast before mouse movement
last_click = 0
ready = False
catch_time = None
wait_time = None
mouse_pos = None

def sound_trigger(indata, frames, time_info, status):
    global last_click, ready, catch_time
    volume = np.linalg.norm(indata)

    if not ready:
        if time.monotonic() - last_click > 2:
            ready = True
            print("🎧 Ready to catch fish...")
        return

    if volume > threshold and time.monotonic() - last_click > cooldown and catch_time is None:
        print("🎣 Catch detected - starting delay")
        catch_time = time.monotonic()

def main_loop():
    global last_click, catch_time, wait_time, mouse_pos
    while True:
        now = time.monotonic()

        if catch_time is not None and now - catch_time > delay_after_sound:
            print("🎣 Performing cast")
            pyautogui.rightClick()
            time.sleep(cast_delay)
            pyautogui.rightClick()
            last_click = now
            wait_time = now
            mouse_pos = pyautogui.position()
            catch_time = None

        if wait_time is not None and now - wait_time > mouse_move_delay:
            print("🖱️ Moving mouse slightly and back")
            x, y = mouse_pos
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            pyautogui.moveTo(x + dx, y + dy, duration=0.2)
            time.sleep(0.2)
            pyautogui.moveTo(x, y, duration=0.2)
            wait_time = None

        time.sleep(0.01)

print(sd.query_devices())
last_click = time.monotonic()

with sd.InputStream(device=31, callback=sound_trigger):
    print("🔊 Listening... wait 2 seconds before it's ready.")
    main_loop()
