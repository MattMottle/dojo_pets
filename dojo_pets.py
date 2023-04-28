class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(f"That was a good walk! Good job {self.pet.name}!")
        return self

    def feed(self):
        if self.pet_food == 0:
            print("Go get some pet food!")
        else:
            self.pet_food = self.pet_food -5
            self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self
    
    def show_treats(self):
        print(f"{self.first_name} has {self.treats} treats")
        return self
    
    def show_pet_food(self):
        print(f"{self.first_name} has {self.pet_food} cans of pet food")
        return self


class Pet:
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.health = 50
        self.energy = 25

    def show_energy(self):
        print(f"{self.name}'s energy is : {self.energy}")
        return self
    
    def show_health(self):
        print(f"{self.name}'s health is: {self.health}")
        return self
    
    def sleep(self):
        self.energy = self.energy + 25
        print(f"Yawn! {self.name} had a good nap!")
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"{self.name} just ate. Yum!")
        return self

    def treat(self):
        self.energy = self.energy + 20
        self.health = self.health - 5
        self.treats = self.treats - 1
        return self

    def play(self):
        self.health = self.health + 5
        return self

    def noise(self):
        if self.pet_type == "dog":
            print(f"{self.name} said: ARF ARF")
        if self.pet_type == "cat":
            print(f"{self.name} said: MEOW MEOW")
        if self.pet_type == "parrot":
            print(f"{self.name} said: Yo Mama so fat when she fell I didn't laugh, but the sidewalk cracked up!")
        return self

class Puddles(Pet):
    def __init__(self):
        super().__init__("Puddles", "dog", ["sit", "lay down", "rollover", "fetch"])

class Meowy(Pet):
    def __init__(self):
        super().__init__("Meowy Poppins", "cat", ["sleep", "scratch", "be sassy"])

class Johnny(Pet):
    def __init__(self):
        super().__init__("Johnny Bananas", "parrot", ["Yo Mama Jokes"])

johnny = Johnny()
meowy = Meowy()
puddles = Puddles()

matt = Ninja("Matt", "Mottle", 20, 5, puddles)
mia = Ninja("Mia","Mottle", 20, 5, meowy)
rachel= Ninja("Rachel","Smith", 20, 5, johnny)


matt.bathe().feed().walk()
rachel.bathe().feed().walk()
mia.bathe().feed().walk()