class Node:
	def __init__(self, value=None, nextEl=None):
		self.next = nextEl
		self.value = value

	def setValue(self, value):
		self.value = value

	def setNext(self, nextEl):
		self.next = nextEl

	def getNext(self):
		return self.next

	def getValue(self):
		return self.value


class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def createHead(self):
		self.head = Node()


	def printLinkedList(self):
		curr = self.head
		while(not (curr==None)):
			print(curr.getValue())
			curr = curr.getNext()

	def insertAfterHead(self, nodeEl):
		Node newnode = nodeEl
		self.head.
