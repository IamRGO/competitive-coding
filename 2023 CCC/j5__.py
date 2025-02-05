word = input()
l = int(input())
w = int(input())
puzzle = []

for i in range(l):
    puzzle.append(input().split())

rules = {
    (1, 1) : [(-1, 1), (1, -1)],
    (-1, -1) : [(-1, 1), (1, -1)],
    (-1, 1) : [(1, 1), (-1, -1)],
    (1, -1) : [(1, 1), (-1, -1)],
    (0, 1) : [(1, 0), (-1, 0)],
    (0, -1) : [(1, 0), (-1, 0)],
    (1, 0) : [(0, 1), (0, -1)],
    (-1, 0) : [(0, 1), (0, -1)]
    }

word_list = []
def search(y, x):
    queue = [(x, y, None, None, [[x, y]])]

    while len(queue) != 0:
        pos = queue.pop(0)
        x, y, curr_dir, t_status, hist = pos

        next_letter = len(hist)
        if next_letter == len(word):
            word_list.append(hist)
            continue
        
        next_dir = [curr_dir]

        if t_status == None:
            next_dir = rules.keys()

        elif t_status == False:
            next_dir += rules[curr_dir]

        for i in next_dir:
            n_y = y + i[0]
            n_x = x + i[1]

            if t_status == None:
                nt_status = False
            else:
                nt_status = t_status or curr_dir != i

            if n_y < 0 or n_x < 0 or n_y >= l or n_x >= w:
                continue

            elif puzzle[n_y][n_x] == word[next_letter]:
                queue.append((n_x, n_y, i, nt_status, hist + [[n_x, n_y]]))


for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        if puzzle[i][j] == word[0]:
            search(i, j)

print(len(word_list))


"""
MENU
5
7
F T R U B L K
P M N A X C U
A E R C N E O
M N E U A R M
M U N E M N S

NATURE
6
9
N A T S F E G Q N
S A I B M R H F A
C F T J C U C L T
K B H U P T A N U
D P R R R J D I R
I E E K M E G B E
"""