import queue
kolejka = queue.Queue()
ticket_number = 1
def f():
    global ticket_number
    kolejka.put(ticket_number)
    print(f'Customer with ticket number {ticket_number} has been added to the queue')