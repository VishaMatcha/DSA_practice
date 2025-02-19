class node:
    def __init__(self,value):
        self.val = value
        self.next = None
        
        
class stack:
    def __init__(self):
        self.head = node('head')
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
        return self.head.next.val
    
def rainwateer(g):
    stored = stack()
    ans = 0
    
    for i in range(len(g)):
        while stored.isEmpty() == False and g[i]> g[stored.peek()]:
            pe = g[stored.pop()]
            
            if stored.isEmpty() == True:
                break
            
            d = i - stored.peek() - 1
            
            mh = min(g[i], g[stored.peek()]) - pe

            ans += mh * d
            
        stored.push(i)
        
    return ans
    
    
g = [4,2,0,3,2,5]
print(rainwateer(g))