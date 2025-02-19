class node:
    def __init__(self,value):
        self.val = value
        self.next = None
        
class queue:
    def __init__(self):
        self.head = node("dummy")
        self.tail = self.head
        self.size = 0
        
    def getsize(self):
        return self.size
    
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    def enqueue(self, value):
        self.tail.next = node(value)
        self.size += 1
        self.tail = self.tail.next
        
    def dequeue(self):
        if self.isEmpty():
            print("stack empty")
            return
        self.size -= 1
        removed = self.head.next
        self.head.next = self.head.next.next
        return removed.val
        
    def front(self):
        if self.isEmpty():
            print("stack is empty")
            return
        return self.head.next.val
    
myq = queue()
myq.enqueue(1)
myq.enqueue(2)
myq.enqueue(3)
print(myq.front())
print(myq.dequeue())
myq.enqueue(4)
print(myq.front())
