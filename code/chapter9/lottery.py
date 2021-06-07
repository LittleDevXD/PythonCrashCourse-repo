import random

class Lottery:
    def __init__(self):
        # Character to form a ticket
        self.chars = ('1', '2', '3', '4', '5', '6', '7', '8', 
                      '9', '10', 'A', 'B', 'C', 'D', 'E')
        self.my_ticket = "123D"

    # Return the ticket of the winner
    def check_winner(self):
        ticket = ""
        while len(ticket) < 4:
            ticket += random.choice(self.chars)
        return ticket

    # Checking the probibility of my ticket
    def my_winning_chance(self):
        count = 0
        while self.check_winner() != self.my_ticket:
            self.check_winner()
            count += 1
        return count


my_lottery = Lottery()

# This seems to go an infinite loop
while my_lottery.my_winning_chance() != 1:
    print(my_lottery.my_winning_chance())
    my_lottery.my_winning_chance()