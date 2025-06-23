class Node:
	def __init__(self, name):
		self.name = name
		self.next = None
		self.prev = None

class DoubleLinkedList:
	def __init__(self):
		self.head = None

	def add(self, name):
		
		new_node = Node(name)
		if self.head is None:
			self.head = new_node
			new_node.next = new_node.prev = self.head
			return 

		current_node = self.head
		new_node.next = self.head
		while current_node.next != self.head:
			current_node = current_node.next
		current_node.next = new_node
		new_node.prev = current_node
		self.head = new_node

	def forward(self, num):
		current_node = self.head
		for x in range(0, num):
			current_node = current_node.next
		return current_node

	def backward(self, num):
		current_node = self.head
		for x in range(0, num):
			current_node = current_node.prev
		return current_node

	def focus(self, name):

		if self.head.name is name:
			return

		current_node =  self.head
		while current_node.next != self.head:
			if current_node.name == name:
				current_node.prev.next = current_node.next
				current_node.next.prev = current_node.prev
				current_node.next = self.head
				current_node.prev = self.head.prev
				self.head = current_node
				return
			current_node = current_node.next

	def current_focus(self):
		if self.head is None:
			print("No tasks")
		else:
			print(self.head.name)

	def close_tab(self, name):
		if self.head is None:
			print("Invalid operation")
		current_node  = self.head
		if current_node.name == name:
			current_node.prev.next = current_node.next
			current_node.next.prev = current_node.prev



tab = DoubleLinkedList()
tab.add('VS Code')
tab.add('Sublime')
tab.add('Postman')
tab.focus('VS Code')
tab.current_focus()
