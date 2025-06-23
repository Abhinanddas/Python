
class Element:
    def __init__(self, value, name):
        self.val =value
        self.next = None
        self.prev = None
        self.name = name


class LinkedList:
    
    def __init__(self):
         
         self.a = Element(0, 'A')
         self.b = Element(0,' B')
         self.c = Element(0, 'C')
         self.d = Element(0, 'D')
         
         self.a.next =self.b
         self.b.next= self.c
         self.c.next =self.d
         self.d.next =self.a
         
         self.a.prev=self.d
         self.b.prev=self.a
         self.c.prev=self.b
         self.d.prev=self.c


    def forward(self,node, rev):
        
        for x in range(rev):
            node.val +=1
            node = node.next
            
    def reverse(self,node, rev):
        for x in range(rev):
            node.val +=1
            node = node.prev
    

    
def fetch_coin_count(total, rev):
    
    ll =LinkedList()
    
    direction = True
    head = ll.a
    while total>0:
        
        count = rev
        
        if (total/rev) < 1:
            count = total % rev
        
        if direction:
            ll.forward(head,count)
            
        if not direction:
            ll.reverse(head, count)
        
        next_head = rev%4
        
        if next_head == 3:
            head = ll.c
        
        if next_head == 1:
                head = ll.a
        
        if next_head == 2:
                head = ll.b
        
        if next_head == 0:
                head = ll.a
            
            
        direction = False if direction else True
        total -= rev     
        
    print(" A::{}, B::{}, C::{}, D::{}".format(ll.a.val, ll.b.val, ll.c.val, ll.d.val))

fetch_coin_count(10,5)
fetch_coin_count(10,4)
fetch_coin_count(20,11)
