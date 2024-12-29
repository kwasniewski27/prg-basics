from ebook import ebook
def main():
    my_ebook = ebook('HP', 'JFK', '380')
    my_ebook.show_status()
    my_ebook.open()
    my_ebook.show_status()
    my_ebook.read(73)
    my_ebook.show_status()
    my_ebook.read(279)
    my_ebook.show_status()
    my_ebook.read(279)
    my_ebook.show_status()
    my_ebook.close()
    my_ebook.show_status()
if __name__ == "__main__":
   main() 