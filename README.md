# 🎣 Auto Fishing Bot (Sound Triggered)

This Python project simulates an automatic fishing action in a game using microphone input. When a sound (like a fish bite) is detected above a certain threshold, the bot performs a right-click action to "catch" the fish.

## 🚀 Features

- Listens to microphone input for sound peaks.
- Automatically performs double right-clicks to simulate casting and catching.
- Moves the mouse slightly after the catch to avoid inactivity detection.
- Uses a delay system to mimic human-like behavior.

## 🧠 How It Works

1. The bot waits 2 seconds after startup to become "ready".
2. It listens to the microphone for sounds louder than the defined threshold.
3. When triggered:
   - It simulates a right-click to cast or catch.
   - Moves the mouse slightly and returns it to prevent AFK detection.

## 🎛️ Requirements

- Python 3.8+
- Microphone input
- Dependencies:
  - `sounddevice`
  - `numpy`
  - `pyautogui`

Install dependencies using pip:

```bash
pip install sounddevice numpy pyautogui
⚙️ Configuration
Make sure to set the correct microphone input device index:

python
Kopiér
Rediger
with sd.InputStream(device=31, callback=sound_trigger):
To find your device index:

python
Kopiér
Rediger
print(sd.query_devices())
You can also tweak the sensitivity and delay settings at the top of the script:

python
Kopiér
Rediger
threshold = 0.1  # Sensitivity to sound
cooldown = 1.0   # Minimum delay between actions
⚠️ Disclaimer
Use at your own risk.
This script simulates user input and may violate the terms of service in some games.
Misuse can result in account suspensions or bans.
The developer is not responsible for any consequences that may occur from using this script.

📄 License
This project is open-source and free to use under the MIT License.
