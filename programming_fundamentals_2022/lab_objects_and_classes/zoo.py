class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return print(f"{species.capitalize()}s in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}")
        elif species == 'fish':
            return print(f"{species.capitalize()}es in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}")
        elif species == 'bird':
            return print(f"{species.capitalize()}s in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}")


name_zoo = input()
zoo = Zoo(name_zoo)
count_animals = int(input())
for digit in range(count_animals):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animals(species, name)
species = input()
zoo.get_info(species)
