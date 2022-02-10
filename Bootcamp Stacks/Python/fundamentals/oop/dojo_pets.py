class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treat = treats
        self.pet_food =  pet_food
        self.pet = Pet()
    def walk(self):
        self.Pet.play(self)
        return self
    def feed(self):
        self.Pet.eat(self)
        return self
    def bathe(self):
        self.Pet.noise(self)
        return self 

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.health = Health()
        self.type = type
        self.tricks = tricks
    def sleep(self):
        self.Health.energy += 50
        return self
    def eat(self):
        if self.Health.hunger < 10:
            self.Health.anger += 5
        else:
            self.Health.hunger -= 20
        return self
    def play(self):
        if self.Health.energy < 15:
            self.Health.anger += 5
        else:
            self.Health.lonliness -= 10
            self.Health.boredom -= 25
            self.Health.energy - 15
    def noise(self):
        pass

class Health:
    def _init__(self,energy=50,hunger=50,boredom=25,lonliness=25,anger=0):
        self.energy = energy
        self.hunger = hunger
        self.boredom = boredom
        self.anger = anger
        self.lonliness = lonliness

class Bird(Pet):
    def __init__(self, name, type, tricks,wing_span,flight):
        super().__init__(name, type, tricks)
        self.name = name
        self.type = type
        self.wing_span = wing_span
        self.flight = flight 
    def fly(self):
        if self.Health.energy < 15:
            self.Health.anger += 5
        else:
            self.Health.energy - 15


class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks);

class Cat(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
