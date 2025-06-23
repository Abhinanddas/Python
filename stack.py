class Stack:
    def __init__(self):
        self.stack=[]
        
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
        return len(self.stack)
    
    def top(self):
        return self.stack[-1]
            

a = Stack()
a.empty()
a.push(10)
a.empty()
a.push(20)
print("The stack contains {n} items".format(n =a.size()))
print("Top element:: {n}".format(n =a.top()))
a.traverse()
a.pop()
    
        