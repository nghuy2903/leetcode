import copy

PACMAN = 'P'
FOOD = 'F'
GHOST = 'G'
EMPTY = '.'

initial_board = [
    [EMPTY, EMPTY, FOOD],
    [EMPTY, EMPTY, EMPTY],
    [PACMAN, EMPTY, GHOST]
]

# Di chuyển: lên, xuống, trái, phải
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def find_pos(board, target):
    for i in range(3):
        for j in range(3):
            if board[i][j] == target:
                return (i, j)
    return None

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic(board):
    pacman = find_pos(board, PACMAN)
    ghost = find_pos(board, GHOST)
    food = find_pos(board, FOOD)

    # Pacman bị bắt
    if pacman is None or (ghost and pacman == ghost):
        return -100

    # Pacman ăn xong
    if food is None:
        return 100

    dist_to_food = manhattan(pacman, food)
    dist_to_ghost = manhattan(pacman, ghost)

    return -2 * dist_to_food + 5 * dist_to_ghost

def get_next_states(board, player):
    states = []
    pos = find_pos(board, player)
    if pos is None:
        return []
    #Duyệt hướng di chuyển
    for dx, dy in directions:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            if player == PACMAN and board[nx][ny] == GHOST:
                continue  # tránh đi vào ma
            #Tạo bàn cờ tương tự và thay đổi vị trí hiện tại
            new_board = copy.deepcopy(board)
            new_board[pos[0]][pos[1]] = EMPTY
            if player == PACMAN and board[nx][ny] == FOOD:
                new_board[nx][ny] = PACMAN  # ăn luôn food
            else:
                new_board[nx][ny] = player
            states.append(new_board)
    return states

def minimax(board, depth, alpha, beta, is_maximizing):
    eval_score = heuristic(board)
    if depth == 0 or eval_score in [100, -100]:
        return eval_score, board

    if is_maximizing:
        max_eval = float('-inf')
        best_state = None
        for state in get_next_states(board, PACMAN):
            eval, _ = minimax(state, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_state = state
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_state
    else:
        min_eval = float('inf')
        best_state = None
        for state in get_next_states(board, GHOST):
            eval, _ = minimax(state, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_state = state
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_state

def run_demo():
    board = initial_board
    depth = 4

    print("Trạng thái ban đầu:")
    print_board(board)

    for turn in range(5):
        score, new_board = minimax(board, depth, float('-inf'), float('inf'), True)
        if new_board is None:
            print("Pacman không còn nước đi!")
            break
        board = new_board
        print(f"Lượt {turn+1} - Pacman di chuyển (score={score}):")
        print_board(board)

        if evaluate(board) in [100, -100]:
            print("Trò chơi kết thúc.")
            break

        score, new_board = minimax(board, depth, float('-inf'), float('inf'), False)
        if new_board is None:
            print("Ma không còn nước đi!")
            break
        board = new_board
        print(f"Lượt {turn+1} - Ma di chuyển (score={score}):")
        print_board(board)

        if evaluate(board) in [100, -100]:
            print("Trò chơi kết thúc.")
            break

run_demo()
