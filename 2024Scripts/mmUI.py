import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import clicktyClack as cc

def start_function():
    radius = radius_entry.get()
    duration = duration_entry.get()
    if(check_radius(radius) and check_duration(duration)):
        status_bar.config(text=f"Started radius={radius} px, duration={duration} min. Please move mouse to stop.")
        cc.dance_mouse(int(radius), int(duration)*60)
    else:
        status_bar.config(text=f"Something went wrong. Please check.")

def stop_function():
    status_bar.config(text=f"Ready")

def check_radius(radius):
    if(radius.isdigit() and int(radius) > 9 and int(radius) < 800):
        return True
    else:
        messagebox.showerror("Error", "Radius must be a number between 10 and 800")
        return False

def check_duration(duration):
    if(duration.isdigit() and int(duration) > 0 and int(duration) < 30):
        return True
    else:
        messagebox.showerror("Error", "Duration must be a number between 1 and 30")
        return False
        

# Create the main window
root = tk.Tk()
root.title("Mouse Dance 🐁")
root.iconphoto(False, tk.PhotoImage(file="C:\\development\\pythonRunner\\assets\\"+"mouse.png"))  # Ensure you have this image in the assets directory

# Add a welcome title and message
title_label = tk.Label(root, text="Welcome to Mouse Dance", font=("Helvetica", 16))
title_label.pack(pady=10)

message_label = tk.Label(root, text="Please ensure the radius and duration values, then click Start.", font=("Helvetica", 12))
message_label.pack(pady=5)

# Add input fields for radius and duration
radius_label = tk.Label(root, text="Radius (pixels):")
radius_label.pack(pady=5)
radius_entry = tk.Entry(root, textvariable="20")
radius_entry.pack(pady=5)

duration_label = tk.Label(root, text="Duration (minutes):")
duration_label.pack(pady=5)
duration_entry = tk.Entry(root, textvariable="1")
duration_entry.pack(pady=5)

#Add status bar
status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Add Start and Stop buttons
start_button = tk.Button(root, text="Start", command=start_function)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_function)
stop_button.pack(pady=5)

# Add a graphic of a dancing mouse
mouse_image = Image.open("C:\\development\\pythonRunner\\assets\\"+"mouse_dancing.gif")  # Ensure you have this image in the assets directory
mouse_image = mouse_image.resize((150, 150))
mouse_photo = ImageTk.PhotoImage(mouse_image)
mouse_label = tk.Label(root, image=mouse_photo)
mouse_label.pack(side="right", padx=10, pady=10)

# Run the application
root.mainloop()