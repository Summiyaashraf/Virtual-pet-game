from pet import Pet

class Game:
    def __init__(self, pet_name):
        self.pet = Pet(pet_name)

    def get_pet(self):
        return self.pet
