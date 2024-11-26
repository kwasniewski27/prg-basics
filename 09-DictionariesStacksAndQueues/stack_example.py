import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts')    
cards.put('Queen of Diamonds')  
cards.put('Jack of Spades')     
cards.put('2')
cards.put('3')
cards.put('7')
cards.put('4')
cards.put('1')
cards.put('9')
cards.put('8')

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
i = 0
first_two = 0
rest = 0
while not cards.empty():
    card = cards.get()
    print(card)
    if i == 0 or i == 1:
        first_two += int(card)
    else:
        if card.isnumeric():
            rest += int(card)
    i += 1
print(first_two)
print(rest)
"""
Note the order of the printed elements.
The last added element is printed first.
"""
