from bank import bank
def main():
    my_bank = bank()
    my_bank.create_account('12 3456 5555 9090 1111 0000 7722')
    my_bank.show_status()
    my_bank.deposit(25.30)
    my_bank.show_status()
    my_bank.withdraw(31.70)
    my_bank.show_status()
    my_bank.withdraw(14)
    my_bank.show_status()
if __name__ == "__main__":
   main() 