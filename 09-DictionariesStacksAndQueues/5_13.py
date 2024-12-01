import queue
stack = queue.LifoQueue()
while True:
    on_stack = input('Enter:')
    if on_stack.isdigit():
        stack.put(int(on_stack))
    elif on_stack in '+ - * /':
        num1 = stack.get()
        num2 = stack.get()
        if on_stack == '+':
            result = num1+num2
        elif on_stack == '-':
            result = num1-num2
        elif on_stack == '*':
            result = num1*num2
        elif on_stack == '/':
            result = num1/num2
        stack.put(result)
    elif on_stack == '=':
        while not stack.empty():
            stackk = stack.get()
            print(stackk)
        break