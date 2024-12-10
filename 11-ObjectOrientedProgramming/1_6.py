class Phone():
    def __init__(self, brand, model, price):
            self.brand = brand
            self.model = model
            self.price = price
    def call(self):
        print("You are calling...")
    def message(self):
         print("Type in your message: ...")
    def play_game(self):
         print("You are playing a game.")
    def info(self):
         print(f"Your phone is: {self.brand} {self.model} and it costs {self.price}")
def main():
    my_phone = Phone("Iphone", 13, "800$")
    my_phone.call()
    my_phone.message()
    my_phone.play_game()
    my_phone.info()
if __name__ == "__main__":
     main()