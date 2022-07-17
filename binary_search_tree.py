class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        
        return self.insert_helper(self.root, new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)
    
    def insert_helper(self, node, new_val):
        
        if node is None:
            return Node(new_val)
            
        if node.value < new_val:
            node.right = self.insert_helper(node.right, new_val)
        else:
            node.left = self.insert_helper(node.left, new_val)
            
        return node
    
    def print_tree(self):
        self.print_in_order(self.root)
        
    def print_in_order(self,node):
        
        if node:
            
            self.print_in_order(node.left)

            print(node.value)
            
            self.print_in_order(node.right)
            
    def search_helper(self, node, find_val):
        
        if node:
              if node.value == find_val:
                  return True
              
              if node.value < find_val:
                  return self.search_helper(node.right, find_val)
              else:
                  return self.search_helper(node.left, find_val)
                   
        return False
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

tree.print_tree()
# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
