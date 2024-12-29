import random
class temperature:
    def __init__(self):
        self.ison = False
    def on(self):
        self.ison = True
    def off(self):
        self.ison = False
    def measure(self):
        self.temperature = random.randrange(34,42)
    def show_status(self):
        if self.temperature >= 37.0 and self.temperature < 41.0:
            print(f'Temperature: {self.temperature}C (fever)')
        elif self.temperature >= 41.0:
            print(f'Temperature: {self.temperature}C (CRITICAL TEMPERATURE!!)')
        else:
            print(f'Temperature: {self.temperature}C ')