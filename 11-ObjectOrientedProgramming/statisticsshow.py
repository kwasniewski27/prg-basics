from statystyka import stat

def main():
    program = stat()
    program.add()
    program.add()
    program.add()
    program.add()
    program.add()
    program.show_status()
    program.greatest()
    program.smallest()
    program.arithmetic()
    program.median()
    program.show_quantities()
if __name__ == "__main__":
    main()