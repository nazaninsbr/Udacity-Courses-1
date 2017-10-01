class Parent:
	def __init__(self, lName):
		print("Parent constructor called")
		self.last_name = lName

	def print_info(self):
		print(self.last_name)

class Child(Parent):
	def __init__(self, lName, n):
		print("Child constructor called")
		Parent.__init__(self, lName)
		self.numberOfToys = n
	def print_info(self):
		print(self.last_name)
		print(self.numberOfToys)

if __name__ == '__main__':
	c = Child("Miley", 20)
	c.print_info()
