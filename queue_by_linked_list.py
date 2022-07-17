class LinkedList:
    def __init__(self, value, next = None):
        self.value = value
        self.next = None


class Queue:
    
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self,value):
        
        element = LinkedList(value)
        if self.front == None and self.rear == None:
             element.next = None
             self.front = element
             self.rear = element
             return
        element.next = self.front
        self.front = element
        return
    
    def dequeue(self):
        
        
        if self.front == None:
            print("No elements in queue.")
            return None
        
        if self.front == self.rear:
            value = self.front.value
            self.front = None
            self.rear = None
            return value
        
        current = self.front
        
        while(current.next):
            prev = current
            current = current.next
        
        self.rear = prev
        prev.next = None
        return current.value
        
    
    def peek(self):
        return self.rear.value if self.rear else None
    
# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print (q.peek())

# Test dequeue
# Should be 1
print (q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print (q.dequeue())
# Should be 3
print (q.dequeue())
# Should be 4
print (q.dequeue())
q.enqueue(5)
# Should be 5
print (q.peek())
