from collections import deque
from numpy import inf


class TreeNode:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.children = [] #danh sách node con
    #Thêm vào danh sách chứa node con - tupple(node con, g)
    def add_child(self, child_node, g):
        self.children.append((child_node, g))
    
def BranchAndBound(root : TreeNode, goal):
    #List node
    queue = deque()
    queue.append((root, 0, 0))
    cost = float(inf) #biến lưu đường đi cần tìm
    flag = False #Cờ để dễ phân biệt được đã tìm được node cần tìm hay chưa
    print(f'{"Current Node".ljust(15)}{"Neighbor".ljust(45)}{"List"}')
    while(queue):

        current, cost_current, f_current = queue.popleft()
        nameNode = current.name
        #Nếu tìm thấy node cần tìm lần, xét điều kiện để cập nhật cost tối ưu hơn và bật cờ lên để bắt đầu loại bỏ các node không tối ưu trong List
        if nameNode == goal:
            if cost_current < cost:
                cost = cost_current
                flag = True
        #Điều kiện để loại bỏ node trong List: Đã tìm được đích, và cost(node of List) > cost(goal)
        if flag == True and f_current > cost:
            print(
                    f'{current.name.ljust(15)}'
                    f'{"f_current: " + str(f_current) + " > cost: " + str(cost):<45}'
                    f'{str([f"{n.name}:{f}" for n, c, f in queue])}'
                )
            continue

        neighborOfCurrent = deque()

        for child, cost_child in current.children:
            total_cost = cost_child + cost_current
            f = total_cost + child.heuristic
            neighborOfCurrent.append((child, total_cost, f))
        #sort danh sách neighbor theo hàm f
        neighborOfCurrent = deque(sorted(neighborOfCurrent, key=lambda x : x[2] ))
        #Duyệt ngược danh sách neighbor để thêm vào List cho đúng
        for node in reversed(neighborOfCurrent):
            queue.appendleft(node)
        print(
            f'{nameNode.ljust(15)}'
            f'{str([f"{n.name}:{f}" for n, c, f in neighborOfCurrent]).ljust(45)}'
            f'{str([f"{n.name}:{f}" for n, c, f in queue])}'
        )

    if flag:
        print(f'{nameNode.ljust(15)}'
                f'Goal: {root.name} -> {goal} : {cost}'
            )
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


BranchAndBound(M, 'R')
