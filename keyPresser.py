from pynput.keyboard import Key, Controller, Listener
import keyboard
import time

keyboardController = Controller()
isRunning = True

print("pressing enter every 200ms, starting in 5 seconds")
print("press f to cancel")
time.sleep(5)

while isRunning:
    keyboardController.press(Key.enter)
    keyboardController.release(Key.enter)
    time.sleep(0.1)
    if keyboard.is_pressed("f"):
        isRunning = False

