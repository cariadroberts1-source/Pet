class Tamagotchi:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 5
        self.health = 5
        self.hunger = 5

    def feed(self):
        self.hunger += 1
        self.happiness += 1
        print(f'{self.name} ate some food!')

    def play(self):
        self.happiness += 2
        self.health += 1
        print(f'{self.name} played and had fun!')

    def check_status(self):
        print(f'Name: {self.name}, Species: {self.species}')
        print(f'Happiness: {self.happiness}, Health: {self.health}, Hunger: {self.hunger}')

    def pass_time(self):
        self.happiness -= 1
        self.hunger -= 1
        if self.happiness < 0:
            self.happiness = 0
        if self.hunger < 0:
            self.hunger = 0

# Example usage:
if __name__ == '__main__':
    poke = Tamagotchi('Pikachu', 'Electric')
    poke.check_status()
    poke.feed()
    poke.play()
    poke.check_status()