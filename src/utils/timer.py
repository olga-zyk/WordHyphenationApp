import time


class Timer:

    def __init__(self):
        self.time_start = 0
        self.time_stop = 0

    def start(self):
        self.time_start = time.time()
        return self.time_start

    def stop(self):
        self.time_stop = time.time()
        return self.time_stop

    def duration(self):
        return self.time_stop - self.time_start
