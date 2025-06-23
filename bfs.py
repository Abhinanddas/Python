class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    
    def __init__(self, root):
        self.root = Node(root)
        
    
    def insert(self, value):
        
        return self.insert_helper(self.root, value)
    
    
    def insert_helper(self, node, value):
        
        if node is None:
            return Node(value)
            
        if value > node.value:
            node.right = self.insert_helper(node.right, value)
        else:
            node.left = self.insert_helper(node.left, value)
        
        return node

    def in_order(self):
        
        return self.in_order_print(self.root)
    
    def in_order_print(self, node):
        
        if node:
            
            self.in_order_print(node.left)
            
            print(node.value)
        
            self.in_order_print(node.right)
    
    def bfs_traversal(self):
        
        if self.root is None:
            return 
        
        queue =[]
        
        queue.append(self.root)
        
        while(len(queue) > 0):
            
            node = queue.pop(0)
            
            print(node.value)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
        
        
tree = BinaryTree(1)
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(2)


tree.in_order()
tree.bfs_traversal()