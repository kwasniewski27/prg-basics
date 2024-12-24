from tv import TV


def main():
   my_tv = TV()
   my_tv.show_status()
   my_tv.on()
   my_tv.show_status()
   my_tv.show_channels()
   my_tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
   my_tv.show_channels()
   my_tv.show_status()
   my_tv.off()
   my_tv.show_status()

if __name__ == "__main__":
   main() 