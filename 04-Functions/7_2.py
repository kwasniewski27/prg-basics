def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    # This block will only execute when the script is run directly
    x = 10
    y = 5
    print(f"Add: {add(x, y)}")
    print(f"Subtract: {subtract(x, y)}")

if __name__ == "__main__":
    main()