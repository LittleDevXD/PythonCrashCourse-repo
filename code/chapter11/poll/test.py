import unittest
from poll import Poll

class PollTest(unittest.TestCase):
    def setUp(self):
        question = "What is your favourite programming language? "
        self.poll = Poll(question)

    def test_poll(self):
        response = ['Python', 'C', 'Java']
        self.poll.get_response(response)
        self.assertIn('Python', self.poll.responses)
        self.poll.show_response()

if __name__ == '__main__':
    unittest.main()
