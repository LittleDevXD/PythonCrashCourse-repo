with open('poll.txt', 'a') as poll:
    name = ' '
    while name:
        name = input("Why do you like programming? ")
        if name:
            poll.write(f"{name}\n")