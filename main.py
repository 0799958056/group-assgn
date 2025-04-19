class Pet:
    def __init__(self, name="Teddy Bear", hunger=4, energy=8, happiness=6):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten. Hunger is now {self.hunger}, happiness is {self.happiness}.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} has slept. Energy is now {self.energy}.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}.")
        else:
            print(f"{self.name} is too tired to play. Let them rest!")

    def get_status(self):
        print(f"{self.name}'s status:\n Hunger: {self.hunger}/10\n Energy: {self.energy}/10\n Happiness: {self.happiness}/10")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)  
        print(f"{self.name} learned a new trick: {trick}! Happiness increased to {self.happiness}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")