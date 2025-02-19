class node:
    def __init__(self,value, indx):
        self.val = value
        self.next = None
        self.index = indx
        
        
class stack:
    def __init__(self):
        self.head = node('head', -1)
        self.size = 0
        
    def getsize(self):
        print("size :", end=" ")
        return self.size
        
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    def push(self,value):
        temp = node(value)
        
        temp.next = self.head.next
        self.head.next = temp
        
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            print("stack empty")
            return
        
        temp = self.head.next
        self.head.next = self.head.next.next
        
        self.size -= 1
        return temp.val
    
    def peek(self):
        if self.isEmpty():
            print("stack empty")
            return
        print("peek :", end=" ")
        return self.head.next.val      
    
def nexgreater(ar):
    ans = [-1]*len(ar)
    ms = stack()
    
    for i in range(len(ar)):
        if ar[i] < ms.peek():
            ms.push(ar[i],i) 
        
        
s = stack()
s.push(1)
print(s.peek())
s.push(2)
print(s.peek())
s.push(3)
print(s.peek())
s.push(4)
print(s.peek())
s.push(5)
print(s.peek())
print(s.getsize())
s.pop()
print(s.peek())
print(s.getsize())