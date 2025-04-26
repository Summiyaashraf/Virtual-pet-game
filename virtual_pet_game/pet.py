class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.cleanliness = 5
        self.mood = 5

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
        self.mood += 1

    def play(self):
        self.mood += 2
        self.hunger += 1
        self.cleanliness -= 1

    def clean(self):
        self.cleanliness = 10
