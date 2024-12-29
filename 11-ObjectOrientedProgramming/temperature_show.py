from temperature import temperature
def main():
    thermometer = temperature()
    thermometer.on()
    thermometer.measure()
    thermometer.show_status()
    thermometer.off()

if __name__ == "__main__":
   main() 