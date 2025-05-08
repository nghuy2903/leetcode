from collections import deque

class TreeNode:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.children = [] #danh sách node con
    #Thêm vào danh sách chứa node con - tupple(node con, g)
    def add_child(self, child_node, g):
        self.children.append((child_node, g))
    
def AStar(root : TreeNode, goal):
    #List node
    queue = deque()
    queue.append((root, 0, 0)) #danh sách lưu trữ dạng (node, g, f)
    print(f'{"Current Node".ljust(15)}{"Neighbor".ljust(45)}{"List"}')
    while(queue):
        current, g_current, f_current = queue.popleft()
        nameNode = current.name
        #Nếu tìm thấy node, in ra và dừng lại
        if nameNode == goal:
            print(f'{nameNode.ljust(15)}'
                  f'Goal: {root.name} -> {goal} : {g_current}'
                )
            return
        #Danh sách node Neighbor of u
        neighborOfCurrent = deque()
        #Duyệt từng tupple (node con, g) trong danh sách node con 
        for child, cost_child in current.children:
            # g = g(child) + g(current)
            total_cost = cost_child + g_current
            # f = g + h(child)
            f = total_cost + child.heuristic
            queue.append((child, total_cost, f))
            neighborOfCurrent.append((child, total_cost, f))

        #sort List theo f
        queue = deque(sorted(queue, key=lambda x : x[2]))
        print(
            f'{nameNode.ljust(15)}'
            f'{str([f"{n.name}:{c}" for n, c, _ in neighborOfCurrent]).ljust(45)}'
            f'{str([f"{n.name}:{f}" for n, c, f in queue])}'
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
