option = int(input('Todo App\n  1. Create\n  2. List\n: '))


if option == 1:
    title = input('Enter title: ')
    description = input('Enter description: ')
    with open('todos.txt', 'a') as f:
        f.write(title)
        f.write('|')
        f.write(description)
        f.write('\n')
    print('Task saved.')
elif option == 2:
    with open('todos.txt', 'r') as f:
        print(f.read())
else:
    print('Please select 1 or 2 only.')