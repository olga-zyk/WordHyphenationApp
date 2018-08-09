import time


class Timer:

    @staticmethod
    def start():
        start = time.time()
        return start

    @staticmethod
    def stop():
        stop = time.time()
        return stop

    @staticmethod
    def measurement(start, stop):
        return stop - start
