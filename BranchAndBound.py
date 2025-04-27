from collections import deque
from numpy import inf


class TreeNode:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.children = []

    def add_child(self, child_node, g):
        self.children.append((child_node, g))
    
def BranchAndBound(root : TreeNode, goal):
    queue = deque()
    queue.append((root, 0))
    cost = float(inf)
    flag = False
    print(f'{"Current Node".ljust(15)}{"Neighbor".ljust(30)}{"List"}')
    while(queue):
        current, cost_current = queue.popleft()
        nameNode = current.name
        
        if nameNode == goal:
            if cost_current < cost:
                cost = cost_current
                flag = True
            
        if flag == True and cost_current > cost:
            print(
                    f'{current.name.ljust(15)}'
                    f'{"cost_current: " + str(cost_current) + " > cost: " + str(cost):<30}'
                    f'{[n.name for n, _ in queue]}'
                )
            continue

        neighborOfCurrent = deque()
        for child, cost_child in current.children:
            total_cost = cost_child + cost_current
            neighborOfCurrent.append((child, total_cost))
        neighborOfCurrent = deque(sorted(neighborOfCurrent, key=lambda x : x[1] ))
        for node in reversed(neighborOfCurrent):
            queue.appendleft(node)
        print(f'{nameNode.ljust(15)}'
                f'{str([f"{n.name}:{c}" for n, c in neighborOfCurrent]).ljust(30)}'
                f'{[n.name for n, _ in queue]}')

    if flag:
        print(f'Goal: A -> G : {cost}')
    else:
        print(f'Not find {goal}')

# Example Tree
#        A(6)
#    (4)/    \(2)
#    B(4)    C(5)
# (5)/ (4)\    \(3)
# D(7)  E(2)   F(6)
#        (2)\   /(1)
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
A.add_child(B, 4)
A.add_child(C, 2)
B.add_child(D, 5)
B.add_child(E, 4)
C.add_child(F, 3)
E.add_child(G, 2)
F.add_child(G, 1)

BranchAndBound(A, 'G')
