with open('pi_digits.txt') as pi_digits:
    lines = ''
    lines = pi_digits.readlines()

pi = ''
for line in lines:
    pi += line.strip()

your_birthday = input("Enter your birthday in mmddyy format: ")

if your_birthday in pi:
    print("Your birthday includes in first million digits of PI!")
else:
    print("Your birthdays does not include in first million digits of PI.")

for i in range(1, 1000_000):
    if your_birthday == pi[i:i+6]:
        print(pi[i:i+6])
        print(i)
