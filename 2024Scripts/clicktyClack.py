import sched
import time
import threading
import keyboard
import pyautogui

sec = 5                  # seconds to wait for the mouse to move.
exit_event = threading.Event()
threads = []

def clickWindowsTwice(scheduler):
    scheduler.enter(sec, 1, clickWindowsTwice, (scheduler,))
    pyautogui.press("win",2,0.9,None,True)

def runnr():
    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(1, 1, clickWindowsTwice, (my_scheduler,))
    my_scheduler.run()

def quiter():
    print("Press q to exit.")
    while not exit_event.is_set():
        if keyboard.is_pressed('q'):
            exit_event.set()
            exit()
            break
        pyautogui.sleep(0.1) # To avoid excessive CPU usage

def main():
    t1 = threading.Thread(target=runnr)
    t2 = threading.Thread(target=quiter)
    threads.append(t1)
    threads.append(t2)
    t1.start()
    t2.start()
    for _ in threads:
        _.join()
    exit()               

if __name__ == "__main__":
    print("Started..")
    main()

