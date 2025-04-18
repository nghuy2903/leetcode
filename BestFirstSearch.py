from collections import deque

class TreeNode:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
    
def BestFirstSearch(root : TreeNode, goal):
    queue = deque()
    queue.append(root)
    visited = set()
    print('Current Node' + '\tNeighbor' + '\tList')
    while(queue):
        current = queue.popleft()
        nameNode = current.name
        
        if nameNode == goal:
            print("Goal")
            return
        neighborOfCurrent = deque()
        visited.add(current.name)
        for child in current.children:
            if child.name not in visited:
                queue.append(child)
        queue = deque(sorted(queue, key=lambda node: node.heuristic))
        print(f'{nameNode}\t\t{[n.name for n in queue]}\t\t{[n.name for n in queue]}')
    print('Not find {goal}')
# Example Tree
#        A(6)
#       /    \
#    B(4)    C(5)
#   /   \      \
# D(7)  E(2)   F(6)
#          \
#          G(0)

# Create nodes
A = TreeNode('A', 6)
B = TreeNode('B', 4)
C = TreeNode('C', 5)
D = TreeNode('D', 7)
E = TreeNode('E', 2)
F = TreeNode('F', 6)
G = TreeNode('G', 0)

# Build tree
A.add_child(B)
A.add_child(C)
B.add_child(D)
B.add_child(E)
C.add_child(F)
E.add_child(G)

BestFirstSearch(A, 'G')