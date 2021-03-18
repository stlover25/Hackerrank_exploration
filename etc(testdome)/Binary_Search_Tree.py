import collections
#collections 모듈의 namedtuple 함수를 통해, Node라는 이름을 가진 배열 자료구조를 만든다. 
#이 배열에는 왼쪽에 위치한 노드와 오른쪽에 위치한 노드, 그리고 해당 노드의 값을 포함하고 있다.

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
