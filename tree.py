from queue import Queue

class node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.orientation = 0

def preorder(currnode):
    if currnode == None:
        return
    print(currnode.val, end = " ")
    preorder(currnode.left)
    preorder(currnode.right)
    
def postorder(currnode):
    if currnode == None:
        return
    postorder(currnode.left)
    postorder(currnode.right)
    print(currnode.val, end = " ")

def inorder(currnode):
    if currnode == None:
        return
    inorder(currnode.left)
    print(currnode.val, end = " ")
    inorder(currnode.right)

def levelorder(r):
    nodes = Queue()
    nodes.put(r)

    while nodes.empty() == False:
        root = nodes.get()
        if root.left:
            nodes.put(root.left)
            
        if root.right:
            nodes.put(root.right)
            
        print(root.val, end=" ")

def leftview(r):
    nodes = Queue()
    nodes.put(None)
    nodes.put(r)
    while nodes.empty() == False:
        root = nodes.get()
        if root == None:
            if nodes.empty() == True:
                break
            nodes.put(None)
            root = nodes.get()
            print(root.val, end=" ")
        if root.left:
            nodes.put(root.left)
        if root.right:
            nodes.put(root.right)
            
def rightview(r):
    nodes = Queue()
    nodes.put(None)
    nodes.put(r)
    while nodes.empty() == False:
        root = nodes.get()
        
        if root == None:
            if nodes.empty():
                break
            nodes.put(None)
            continue
        if nodes.queue[0] == None:
            print(root.val, end = " ")
        if root.left:
            nodes.put(root.left)
        if root.right:
            nodes.put(root.right)
            
def topview(r):
    nodes = Queue()
    visited = dict()
    nodes.put(r)
    
    while nodes.empty() == False:
        root = nodes.get()
        root_ori = root.orientation
        
        if root_ori not in visited:
            visited[root_ori] = root.val
        
        if root.left:
            root.left.orientation = root_ori - 1
            nodes.put(root.left)
        if root.right:    
            root.right.orientation = root_ori + 1
            nodes.put(root.right)
            
    for i in sorted(visited):
        print(visited[i], end = " ")

def bottomview(r):
    nodes = Queue()
    visited = dict()
    nodes.put(r)
    
    while nodes.empty() == False:
        root = nodes.get()
        root_ori = root.orientation
        visited[root_ori] = root.val
        
        if root.left:
            root.left.orientation = root_ori - 1
            nodes.put(root.left)
        if root.right:    
            root.right.orientation = root_ori + 1
            nodes.put(root.right)
            
    for i in sorted(visited):
        print(visited[i], end = " ")     


root = node(1)

root.left = node(2)
root.right = node(3)

root.left.left = node(4)
root.left.right = node(5)

root.right.right = node(6)

root.right.right.left = node(7)
node.right.right.right = 

print("preorder: ", end = " ")
preorder(root)
print()
print("inorder: ", end = " ")
inorder(root)
print()
print("postorder: ", end = " ")
postorder(root)
print()
print("BFS: ", end = " ")
levelorder(root)
print()
print("left view: ", end = " ")
leftview(root)
print()
print("right view: ", end = " ")
rightview(root)
print()
print("top view: ", end = " ")
topview(root)
print()
print("bottom view: ", end = " ")
bottomview(root)
print()