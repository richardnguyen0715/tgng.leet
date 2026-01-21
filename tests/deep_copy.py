import copy

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
    
    
x = Node(1)
y = Node(2)
z = Node(3)
x.next = y
y.next = z
x.random = z
z.random= y


# k = [copy.copy(x), copy.copy(y), copy.copy(z)]

# for i in k:
#     if i.random != None:
#         print(i.random.val)
#     else:
#         print(-1)

new_head = copy.copy(x)

runNode = x

while runNode != None:
    new_head