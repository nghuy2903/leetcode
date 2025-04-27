from collections import deque

class TreeNode:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.children = []

    def add_child(self, child_node, g):
        self.children.append((child_node, g))
    
def AStar(root : TreeNode, goal):
    queue = deque()
    queue.append((root, 0, root.heuristic))
    visited = set()
    print(f'{"Current Node".ljust(15)}{"Neighbor".ljust(30)}{"List"}')
    while(queue):
        current, cost_current, f_current = queue.popleft()
        nameNode = current.name
        
        if nameNode == goal:
            print(f'{nameNode.ljust(15)}'
                  f'Goal: {root.name} -> {goal} : {cost_current}'
                )
            return
        neighborOfCurrent = deque()
        visited.add(current.name)
        for child, cost_child in current.children:
            if child.name not in visited:
                total_cost = cost_child + cost_current
                f = total_cost + child.heuristic
                queue.append((child, total_cost, f))
                neighborOfCurrent.append((child, total_cost, f))
        queue = deque(sorted(queue, key=lambda x : x[2]))
        print(
            f'{nameNode.ljust(15)}'
            f'{str([f"{n.name}:{c}" for n, c, _ in neighborOfCurrent]).ljust(30)}'
            f'{[n.name for n, _, _ in queue]}'
        )
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
A = TreeNode('A', 40)
B = TreeNode('B', 30)
C = TreeNode('C', 30)
D = TreeNode('D', 35)
E = TreeNode('E', 2)
R = TreeNode('R', 0)
M = TreeNode('M', 25)

# Build tree
A.add_child(B, 2)
A.add_child(R, 30)
B.add_child(A, 1)
B.add_child(C, 12)
B.add_child(E, 3)
B.add_child(D, 3)
C.add_child(E, 2)
C.add_child(D, 6)
D.add_child(R, 21)
D.add_child(E, 5)
E.add_child(R, 40)
M.add_child(B, 8)
M.add_child(A, 5)
M.add_child(D, 4)
M.add_child(E, 1)


AStar(M, 'R')
