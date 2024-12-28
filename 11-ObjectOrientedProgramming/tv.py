class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channels = []
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def set_channel(self, new_channel_no):
        if 1<= new_channel_no<=len(self.channels):
            self.channel = new_channel_no
        else:
            print('Invalid channel')
    def set_channels(self, channels_list):
        self.channels = channels_list
    def show_channels(self):
        if self.channels:
            print('Available channels:')
            for index, name in enumerate(self.channels, start=1):
                print(f'{index}.{name}')
        else:
            print('There is no channels')
    def show_status(self):
        if self.is_on:
            if 1 <= self.channel <= len(self.channels):
                channel_name = self.channels[self.channel - 1]
            else:
                channel_name = 'no_channel'
            print(f'Tv is on, channel: {self.channel}, {channel_name}')
        else:
            print('Tv is off')