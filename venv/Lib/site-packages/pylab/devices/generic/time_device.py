import time

class TimeDevice():

    def __init__(self):
        self.start_time = time.time()

    def reset_start_time(self):
        self.start_time = time.time()

    def elapsed_time(self):
        return time.time() - self.start_time
