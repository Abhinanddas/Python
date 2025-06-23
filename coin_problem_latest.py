class Node:

	def __init__(self, label):
		self.label = label
		self.counter = 0
		self.left = None
		self.right = None

class DoubleLinkedList():

	def __init__(self):
		self.head = None
		self.tail = None
		self.rotate_clockwise = True

	def add_node(self, label):
		
		new_node = Node(label)
		if self.tail is None:
			self.head = self.tail = new_node.left = new_node.right = new_node
			return

		new_node.left = self.tail
		new_node.right = self.head
		self.tail.right = self.head.left = self.tail = new_node

	def rotate(self, num):
		if self.head is None:
			return
		current_node = self.head
		for x in range(num):
			current_node.counter +=1
			if self.rotate_clockwise:
				current_node = current_node.right
			else:
				current_node = current_node.left
		self.head = current_node.left if self.rotate_clockwise  else current_node.right

	def traverse_forward(self):
		if self.head is None:
			print("Empty")

		current_node = self.head
		print("{name}::{counter}".format(name = current_node.label, counter = current_node.counter))
		while current_node.right != self.head:
			current_node = current_node.right
			print("{name}::{counter}".format(name = current_node.label, counter = current_node.counter))

	def traverse_reverse(self):
		if self.head is None:
			print("Empty")

		print("heading...")
		current_node = self.head 
		while current_node.left != self.head:
			current_node = current_node.left
			print("Node {name} contains {counter} coins".format(name = current_node.label, counter = current_node.counter))
		print("Node {name} contains {counter} coins".format(name = self.head.label, counter = self.head.counter))


def get_coin_count(num_of_coins, reverse_num, member_count = 4):
	linked_list = DoubleLinkedList()
	for i in range(65, 65 + member_count):
		linked_list.add_node(chr(i))

	while reverse_num < num_of_coins:
		linked_list.rotate(reverse_num)
		linked_list.rotate_clockwise = not linked_list.rotate_clockwise
		num_of_coins -= reverse_num 

	linked_list.rotate(num_of_coins)
	linked_list.traverse_forward()

get_coin_count(10, 5)
get_coin_count(10, 4)
get_coin_count(20, 11)