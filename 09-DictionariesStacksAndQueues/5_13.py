import queue
stack = queue.LifoQueue()
while True:
    print('Number to push it on stack')
    print('Operation to calculate two last elements with this operation: ')
    print('Equal sign to display final sum')
    something = input('Enter: ')
    if something.isdigit():
        stack.put(int(something))
    elif something in '+*-/':
        first = stack.get()
        second = stack.get()
        if something == '+':
            result = first + second
        elif something == '*':
            result = first * second
        elif something == '-':
            result = first - second
        elif something == '/':
            result = first/second
        stack.put(result)
    elif something == '=':
        if not stack.empty():
            expression = stack.get()
            print(expression)
            break