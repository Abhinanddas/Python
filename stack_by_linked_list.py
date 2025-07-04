class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, num):

        new_node = Node(num)
        if self.head is None:
            self.head = new_node
            self.size +=1
            return

        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):

        if self.head is None:
            print("The stack is empty.")
            return

        print("The node is {value}".format(value = self.head.value))
        self.head = self.head.next
        self.size -= 1


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
