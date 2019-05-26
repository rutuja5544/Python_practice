# class student:
# 	def __init__(self, n,a):
# 		self.Full_Name = n
# 		self.Age = a

# 	def get_age(self):
# 		return self.Age 


# stud1 = student("Rutuja" , 24)

# print(stud1.Full_Name)
	
class User:
	active_users = 0
	def __init__(self, fname, lname, age):
		self.fname = fname
		self.lname = lname
		self.age = age
		User.active_users += 1

	def active(self):
		return f"{User.active_users} users are active now..!!"

	def logout(self):
		User.active_users -= 1
		return f"{self.fname} has logged out."

	def full_name(self):
		return f"My full name is {self.fname} {self.lname}. Please to meet you..!!"

	def initials(self):
		return f"Initials are {self.fname[0].upper()}.{self.lname[0].upper()}."

	def likes(self,thing):
		return f"{self.fname} likes {thing}"

	def age1(self):
		print(self.age)

user1 = User("Joe","Doe","25")
print(user1.active())
user2 = User("Blanca","Jane","36")
print(user2.active())
user2.logout()
print(user2.active())

# print(user1.likes("ice-cream"))
# print(user2.likes("roaming"))
# print(user1.age1())
# print(user2.age1())
# print(user1.lname)
# print(user1.full_name())
# print(user2.full_name())
# print(user1.initials())
# print(user2.initials())