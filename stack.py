from inspect import stack


class Stack:
    def __init__(self):
        self.stack=[];
        self.head = 0
        
    def push(self,num):
        self.stack.append(num)
        
    def pop(self):
        print("Popped element is ",self.stack.pop())
        
    def traverse(self):
        for x in self.stack:
            print(x)
            
    def empty(self):
        if (len(self.stack) ==0):
            print("Stack is empty")
            return True
        else:
            print("Stack is not empty")
            return False

    def size(self):
        return self.head
    
    def top(self):
        return self.stack[-1]
            

a = Stack();
a.empty()
a.push(10)
a.empty()
a.push(20)
a.size()
a.traverse()
a.pop()
    
        