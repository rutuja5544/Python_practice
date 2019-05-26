
class Pets :
	allowed = ('dog','cat','pig','rat')
	no_of_pets = 0

	def __init__(self, species, pname, pcolor, pfood ):
		if species not in Pets.allowed:
			raise ValueError(f"You can't select {species} as Pet.")
		self.species = species
		self.pname = pname
		self.pcolor = pcolor
		self.pfood = pfood 
		Pets.no_of_pets += 1

	def count(self):
		return f"{Pets.no_of_pets}"

	def info(self):
		return f"Hi, I am a {self.species}, my pet name is {self.pname} , colour is {self.pcolor} , favourite food is {self.pfood}"

# cat = Pets("kity","white","milk")
# dog = Pets("Bruno","Brown","cookies")

# tigey = Pets("tiger", "sheru", "yellow", "meat")
tigey = Pets("dog", "sheru", "yellow", "meat")
print(tigey.info())
print(Pets.allowed)
Pets.allowed.append("cow")
print(Pets.allowed)

# print(cat.info())
# print(dog.info())



		