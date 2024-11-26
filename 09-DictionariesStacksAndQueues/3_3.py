import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = []
    matching_brackets = {'{':'}', '[':']', '(':')'}
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if char == stack[-1]:
                return True
            stack.pop() #True if brackets in expression are ok of False otherwise
if brackets_ok(expression1):
   print("Pierwszy napis jest dobrze")
else:
   print("Pierwszy napis jest źle")

if brackets_ok(expression2):
    print("drugi napis jest dobrze")
else:
   print("drugi napis jest źle")
if brackets_ok(expression2):
    print("Trzeci napis jest dobrze")
else:
   print("Trzeci napis jest źle")