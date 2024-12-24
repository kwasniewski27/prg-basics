class TV:
    def __init__(self):
        self.is_on = False
        self.channel = '1'
        self.channels_tv = []
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def set_channel(self, new_channel_no):
        if new_channel_no in self.channels_tv:
            self.channel = new_channel_no
        else:
            print('There is no such channel')
    def set_channels(self, channels_list):
        self.channels_tv = channels_list
    def show_channels(self):
        if self.channels_tv:
            print("Availaible channels: ")
            for number, name in self.channels_tv:
                print(f'{number}:{name}')
        else:
            print('There is no channels yet')
    def show_status(self):
        if self.is_on:
            channel_name = ''
            for number, name in self.channels_tv:
                if number == self.channel:
                    channel_name = name
                    break
            print(f"Tv is on, channel: {self.channel} ({channel_name})")
        else:
            print(f"Tv is off")