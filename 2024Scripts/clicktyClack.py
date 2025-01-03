import pyautogui
import time
import math
import multiprocessing
import keyboard


def move_mouse_in_circle(radius, interval):
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = pyautogui.position()
    while True:
        for angle in range(0, 360, 10):
            x = center_x + radius * math.cos(math.radians(angle))
            y = center_y + radius * math.sin(math.radians(angle))

            if 0 <= x <= screen_width and 0 <= y <= screen_height:
                pyautogui.moveTo(x, y, 0.001)
            else:
                print("Mouse movement out of screen bounds. Adjusting position.")
                center_x, center_y = pyautogui.position()
                break
        time.sleep(interval)


def listen_for_input(stop_event):
    initial_position = pyautogui.position()
    while not stop_event.is_set():
        if keyboard.is_pressed('q') or keyboard.is_pressed('e'):
            print("Key pressed. Stopping the script.")
            stop_event.set()
            break
        current_position = pyautogui.position()
        if math.hypot(current_position[0] - initial_position[0], current_position[1] - initial_position[1]) > 50:
            print("Mouse moved manually. Stopping the script.")
            stop_event.set()
            break
        time.sleep(0.1)

def read_if_not_empty(r,d):
    if (r is not None and d is not None and r != "" and d != ""):
        print("All set; no changes to radius or duration needed.")
        return r, d
    else:
        return 20, 10 

if __name__ == "__main__":
    radius = input("Enter the radius in pixels (default is 20 pixels): ")
    duration = input("Enter the duration in seconds (default is 10 seconds): ")
    radius, duration = read_if_not_empty(radius, duration)
    
    stop_event = multiprocessing.Event()
    mouse_process = multiprocessing.Process(target=move_mouse_in_circle, args=(int(radius), float(duration)))
    input_process = multiprocessing.Process(target=listen_for_input, args=(stop_event,))

    mouse_process.start()
    input_process.start()

    input_process.join()
    stop_event.set()
    mouse_process.terminate()
 
