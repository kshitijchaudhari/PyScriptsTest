import tkinter as tk
from tkinter import Text, filedialog
import os
from random import seed
from random import randint
import time
import threading

from RepeatingTimer import RepeatingTimer

__timer = 5
__height = 500
__width = 700

root = tk.Tk()


def appStart():
    t = threading.Thread(target={r.run()})
    t.start()


def resetScore():
    r.stop()


def generateApples():
    o = seed(int(round(time.time() / 1000)))
    a = tk.PhotoImage(file="assets/apple.gif")
    x = randint(0, (__width - 20))
    y = randint(0, (__height - 20))
    s = " x: " + str(x) + " , " + " y: " + str(y) + "   seed: " + str(o)
    l1.config(text=s)
    canvas.create_image(x, y, image=a, anchor=tk.NW)


canvas = tk.Canvas(root, height=__height, width=__width, bg="#213209")
canvas.pack()
b1 = tk.Button(root, text="Start", bg="#aaa", command=appStart, justify=tk.LEFT, padx=10)
b1.pack(side="left")
b2 = tk.Button(root, text="Reset High Score", bg="#aaa", command=resetScore, justify=tk.LEFT, padx=10)
b2.pack(side="left")
l1 = tk.Label(root, text="Score Label", justify=tk.LEFT, padx=10)
l1.pack(side="right")
l2 = tk.Label(root, text="Score: ", justify=tk.LEFT, padx=10)
l2.pack(side="right")

r = RepeatingTimer(3, generateApples())

root.mainloop()
