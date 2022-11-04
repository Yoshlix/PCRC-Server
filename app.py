from flask import Flask
import pyautogui

app = Flask(__name__)


@app.route('/space')
def pause():  # press space for playing pause audio/video
    pyautogui.press('space')
    return 'space pressed'


@app.route('/volumeup')
def volUp():  # press the volume up key
    pyautogui.press('volumeup')
    return 'volumeup pressed'


@app.route('/volumedown')
def volDown():  # press volume down key
    pyautogui.press('volumedown')
    return 'volumedown pressed'


@app.route('/lock')
def lock():  # lock your pc
    pyautogui.hotkey('win', 'r')  # windows_key + Run

    pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n")
    return 'lock pressed'


@app.route('unlock/<pin>')
def unlock(pin):  # unlock your pc
    pyautogui.press('space')
    pyautogui.typewrite(pin)

    return 'unlocked'


if __name__ == '__main__':
    app.run(port=6969, host="0.0.0.0")
