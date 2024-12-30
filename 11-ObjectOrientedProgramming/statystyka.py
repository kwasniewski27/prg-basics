import statistics
class stat:
    def __init__(self):
        self.numbers = []
    def add(self):
        number = int(input('Enter number: '))
        self.numbers.append(number)
    def greatest(self):
        return max(self.numbers)
    def smallest(self):
        return min(self.numbers)
    def arithmetic(self):
        return sum(self.numbers) / len(self.numbers)
    def median(self):
        return statistics.median(self.numbers)
    def show_status(self):
        print(" ".join(map(str, self.numbers)))
    def show_quantities(self):
        print(f'Greatest number is: {self.greatest()}, The smallest number is {self.smallest()}, Arithmetic mean: {self.arithmetic():.2f}, Median: {self.median()}')