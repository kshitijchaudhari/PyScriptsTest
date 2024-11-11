import pyautogui
import threading
import time
import random
import keyboard

sec = 60.0                  #the float of seconds to wait for the mouse to move.
event = threading.Event()
width, height = pyautogui.size()

def moveMouse():
    #print("Screen resolution: ", width, " x ", height)
    x = generateCoords(width)
    y = generateCoords(height)
    pyautogui.moveTo(x, y, duration = 0.4)  #coordinates to move the mouse to and the duration taken for the mouse movement

def generateCoords(maxInt):
    s = random.seed(time.time() * 1000)             #initial seeding for random function
    #print("Random seed is -->", s)
    r = random.randint(0,maxInt)             #generating a random integer between lower and higher values for the mouse movement
    #print("generated random intger: ", r)
    return r

def on_key_press(keyEvent):
    if keyEvent.name == 'q' or 'c' or 'e' or 'x':
        event.set()     # Set the event to trigger closing of all open threads

def main():
    t1 = threading.Timer(sec, moveMouse)
    while not event.is_set():
        t1.start()
        t1.join()
        t1 = threading.Timer(sec, moveMouse)
        keyboard.on_press(on_key_press)     # Keyboard listener for key press/down/up events

main()