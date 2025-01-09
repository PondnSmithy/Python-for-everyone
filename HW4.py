expenses = ['Food','Water']

while True:

    receive = input("Please enter expenses: ")

    expenses.append(receive)

    if receive == 'remove':
        expenses.remove('remove')
        expenses.pop()
    
    if len(expenses) == 0 or 'Done' in expenses:
        expenses.remove('Done')
        print(expenses)
        break

    print(expenses)
    