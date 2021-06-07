with open('guest_book.txt', 'w') as guest_book:
    name = " "
    while name:
        name = input("Enter your name sir: ")
        if name:
            guest_book.write(f"- {name}\n")
            print(f"Hello {name}")