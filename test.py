class TV:
    def __init__(self):
        self.is_on = False
        self.channel = '1'
        self.channels_tv = []  # Lista krotek (numer, nazwa)

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        if any(number == new_channel_no for number, _ in self.channels_tv):
            self.channel = new_channel_no
        else:
            print('There is no such channel')

    def set_channels(self, channels_list):
        # Oczekujemy listy krotek [(numer, nazwa), ...]
        self.channels_tv = channels_list

    def show_channels(self):
        if self.channels_tv:
            print("Available channels: ")
            for number, name in self.channels_tv:
                print(f'{number}: {name}')
        else:
            print('There are no channels yet')

    def show_status(self):
        if self.is_on:
            # Znajdź nazwę kanału
            channel_name = "Unknown"
            for number, name in self.channels_tv:
                if number == self.channel:
                    channel_name = name
                    break
            print(f"Tv is on, channel: {self.channel} ({channel_name})")
        else:
            print("Tv is off")
