import random

class StateMachine:
    def __init__(self):
        self.state = "generate"
        self.numbers = []
        self.low_numbers = []
        self.high_numbers = []

    def generate_numbers(self):
        self.numbers = [random.randint(0, 10) for _ in range(10)]
        self.state = "filter"

    def filter_numbers(self):
        self.low_numbers = [num for num in self.numbers if 0 <= num <= 4]
        self.high_numbers = [num for num in self.numbers if 5 <= num <= 10]
        self.state = "print"

    def print_numbers(self):
        print("Generated numbers:", self.numbers)
        print("Numbers from 0 to 4:", self.low_numbers)
        print("Numbers from 5 to 10:", self.high_numbers)
        self.state = "done"

    def run(self):
        if self.state == "generate":
            self.generate_numbers()
        elif self.state == "filter":
            self.filter_numbers()
        elif self.state == "print":
            self.print_numbers()

# Opprett og kjør tilstandsmaskinen
sm = StateMachine()
while sm.state != "done":
    sm.run()