class Element():
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    
    def __init__(self, head= None):
        self.head = head
        
    
    def append(self, new_element):
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_element
            
            
    def insert_first(self, new_element):
        self.head = new_element
            
    def delete_first(self):
        
        value = None
        if self.head:
            value = self.head.value
            self.head = self.head.next
        return value
    
class Stack:
    
    def __init__(self, top= None):
        self.ll = LinkedList(top)
        
    def push(self, new_element):
        
        if self.ll.head == None:
            self.ll.insert_first(new_element)
            return
        
        self.ll.append(new_element)
       
    def pop(self):
        
        if self.ll.head == None:
            return None
        
        current = self.ll.head
        prev = None
        if current.next:
            while current.next:
                prev = current
                current = current.next
            prev.next = None
        else:
            self.ll.delete_first()
        return current

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack()


# Test stack functionality
stack.push(e1)
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop())
stack.push(e4)
print (stack.pop().value)