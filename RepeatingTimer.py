import threading


class RepeatingTimer(threading.Thread):
    def __init__(self, interval_seconds, callback):
        super().__init__()
        self.stop_event = threading.Event()
        self.interval_seconds = interval_seconds
        self.callback = callback

    def run(self):
        while not self.stop_event.wait(self.interval_seconds):
            self.callback()

    def stop(self):
        self.stop_event.set()
