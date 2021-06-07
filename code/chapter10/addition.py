while True:
    try:
        f_num = int(input("Enter a number: "))
        s_num = int(input("Enter a number to add: "))
    except ValueError:
        print("Expected number not string.")
    else:
        print(f_num + s_num)
