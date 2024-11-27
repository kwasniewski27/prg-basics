import queue
def f(word):
    stack = queue.LifoQueue()
    for i in word:
        stack.put(i)
    reversed_word=''
    while not stack.empty():
        reversed_word += stack.get()
    print(reversed_word)
word = input("Enter name to reverse: ")
f(word)