class Poll:
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(f"{self.question}")

    def get_response(self, response):
        for resp in response:
            self.responses.append(resp)

    def show_response(self):
        print("Thank you for participating in the poll!")
        for resp in self.responses:
            print(f'- {resp}')

