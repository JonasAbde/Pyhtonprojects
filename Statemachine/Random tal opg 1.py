import random

class StateMachine:
    def __init__(self):
        self.state = self.state1
        self.numbers = []
        self.list1 = []
        self.list2 = []

    def run(self):
        while self.state:
            self.state()

    def state1(self):
        print("State 1: Generer 20 tilfældige tal mellem 0 og 10")
        self.numbers = [random.randint(0, 10) for _ in range(20)]
        print("Genererede tal:", self.numbers)
        self.state = self.state2  # Skift til næste tilstand

    def state2(self):
        print("\nState 2: Sorter tallene i to nye lister")
        self.list1 = [num for num in self.numbers if 0 <= num <= 4]
        self.list2 = [num for num in self.numbers if 5 <= num <= 10]
        self.state = self.state3  # Skift til næste tilstand

    def state3(self):
        print("\nState 3: Print listerne ud på skærmen")
        print("Liste med tal mellem 0 og 4:", self.list1)
        print("Liste med tal mellem 5 og 10:", self.list2)
        self.state = self.stop  # Skift til afslutningstilstand

    def stop(self):
        print("Stop: Programmet afsluttes.")
        self.state = None  # Sluttilstand for at afslutte løkken

if __name__ == "__main__":
    sm = StateMachine()
    sm.run()
