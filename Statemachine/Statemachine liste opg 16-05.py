class StateMachine:
    def __init__(self):
        self.state = self.state1
        self.numbers = []  # Liste med tal der overføres mellem tilstande

    def run(self):
        while self.state:
            self.state()

    def state1(self):
        print("State 1: Indtast 10 tal")
        self.numbers = [int(input(f"Indtast tal {i+1}: ")) for i in range(10)]
        self.state = self.state2

    def state2(self):
        print("\nState 2: Menu")
        print("1. Tilføj flere tal")
        print("2. Find maks og min")
        print("3. Sorter tallene")
        print("4. Afslut programmet")
        choice = input("Vælg en mulighed: ")
        if choice == "1":
            self.state = self.state3
        elif choice == "2":
            self.state = self.state4
        elif choice == "3":
            self.state = self.state5
        elif choice == "4":
            self.state = self.exit_program
        else:
            print("Ugyldigt valg, prøv igen.")
            self.state = self.state2

    def state3(self):
        print("State 3: Tilføj flere tal")
        more_numbers = int(input("Hvor mange flere tal vil du tilføje? "))
        for i in range(more_numbers):
            self.numbers.append(int(input(f"Indtast tal {i+1}: ")))
        self.state = self.state6

    def state4(self):
        print("State 4: Find maks og min")
        if self.numbers:
            print(f"Maks tal: {max(self.numbers)}")
            print(f"Min tal: {min(self.numbers)}")
        else:
            print("Listen er tom.")
        self.state = self.state2

    def state5(self):
        print("State 5: Sorter tallene")
        self.numbers.sort()
        print("Sorterede liste:", self.numbers)
        self.state = self.state2

    def state6(self):
        print("State 6: Tæl antal tal i listen")
        print(f"Listen har nu {len(self.numbers)} tal.")
        self.state = self.state2

    def exit_program(self):
        print("Afslutter programmet.")
        self.state = None  # Sluttilstand for at afslutte løkken

if __name__ == "__main__":
    sm = StateMachine()
    sm.run()
