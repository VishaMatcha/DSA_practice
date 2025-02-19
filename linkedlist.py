class node:
    def __init__(self, value):
        self.val = value
        self.next = None
        

class linkedlist:
    head = None
    
    def printlist(self):
        temp = self.head
        while temp != None:
            print(temp.val,end = " ")
            temp = temp.next
        print(" ")
        
    def insertatlast(self, value):
        if self.head == None:
            self.head = node(value)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
            
        temp.next = node(value)
        
    def inserthead(self, value):
        temp = node(value)
        temp.next = self.head
        self.head = temp

    def insertAt(self, value, k):
        if k==0:
            inserthead(value)
            return 
        c=2
        temp = self.head
        while c<k and temp!=None:
            c+=1
            temp = temp.next
            
        if c<k:
            print("position greater than length")
            return
        
        rest = temp.next
        temp.next = node(value)
        temp.next.next = rest
        
        
    def deletion(self, k):
        if k==0:
            self.head = self.head.next
        c=2
        temp = self.head
        while c<k and temp != None:
            c += 1
            temp = temp.next
        if c<k:
            print("list is smaller than the given index")  
        temp.next = temp.next.next
        
    def middle(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.val
    
    newhead = None
    
    def reverse(self):
        prev = None
        curr = self.head
        
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        self.head = prev
        
        
    
ll = linkedlist()
ll.insertatlast(2)
ll.insertatlast(5)
ll.insertatlast(6)
ll.insertatlast(3)
ll.insertatlast(21)
ll.insertAt(49,3)
ll.inserthead(43)
ll.printlist()
print("middle :",ll.middle())
ll.deletion(3)
ll.printlist()
print("middle :",ll.middle())
ll.reverse()
print("Reversed list : ")
ll.printlist()