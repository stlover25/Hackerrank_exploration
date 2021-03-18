import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    
    temp = root.value
    
    while (temp != value) and (root != None):
        
        if temp < value:
            root = root.right
        
        else:
            root = root.left
        #print(temp)
        
        if root != None:
            temp = root.value
 
    
    if temp == value:
        return True
    
    else:
        return False

n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))
