class Parent:
	def __init__(self, lName):
		print("Parent constructor called")
		self.last_name = lName

class Child(Parent):
	def __init__(self, lName, n):
		print("Child constructor called")
		Parent.__init__(self, lName)
		self.numberOfToys = n

if __name__ == '__main__':
	c = Child("Miley", 20)
