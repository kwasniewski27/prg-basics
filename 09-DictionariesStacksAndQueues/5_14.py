import queue
kolejka = queue.Queue()
kolejka.put(1)
kolejka.put(2)
kolejka.put(3)
while True:
    ticket = input('Enter 1 to withdraw a ticket or 2 to serve a costumer who is first: ')
    if ticket == '1':
        number = kolejka.queue[-1]+1
        kolejka.put(number)
        print(f'Your ticket number is: {number}')
    elif ticket == '2':
        if kolejka.empty():
            print('There is noone to be served')
        else:
            element = kolejka.get()
            print(f'Person with ticket number {element} is being served')
    elif ticket.lower() == 'exit':
        print('Exiting the system.')
        break
    else:
        print('Invalid input. Please enter 1 or 2.')
