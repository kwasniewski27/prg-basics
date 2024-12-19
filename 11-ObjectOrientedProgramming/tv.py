class TV:
    def __init__(self):
        self.is_on = True
        self.channel = '1'
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f"Tv is on, channel: {self.channel}")
        else:
            print(f"Tv is off")