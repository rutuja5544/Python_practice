class Student :
	def __init__(self,fname,lname,std,marks):
		self.fname = fname
		self.lname = lname 
		self.std = std
		self.marks = marks

	def full_name(self):
		return f"{self.fname} {self.lname}"

	def standard(self):
		return f"{self.std}"

	def year_marks(self):
		return f"{self.marks}%"

	def good_things(self,things):
		return f"{self.fname} good in {things} ."

AB = Student("AB","AABB","4th",80)

print(AB.full_name())
print(AB.standard())
print(AB.year_marks())
print(AB.good_things("Maths Subject"))