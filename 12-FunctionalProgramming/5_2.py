from functools import reduce
numbers = [2,4,6,3,7,5]
def add(x, y):
    return x+y
parzyste = filter(lambda x:x%2==0, numbers)
result = reduce(add, parzyste)
print(result)