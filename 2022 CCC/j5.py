n = int(input())
trees = []

for i in range(int(input())):
    trees.append(list(map(int, input().split())))

trees.sort(key = lambda x : x[1])

corners = [[0, 0], [0, n], [n, 0], [n, n]]

for i in range(len(trees)):
    field = trees[i + 1:]

    field = sorted(field, key = lambda x: abs(x[1] - trees[i][1])) 

    i_tl = []
    i_tr = []
    i_bl = []
    i_br = []

    a = [i_tl, i_tr, i_bl, i_br]

    for j in trees:
        if j != trees[i]:
            if j[0] <= trees[i][0] and j[1] >= trees[i][1]:
                i_tr.append(j)

            if j[0] <= trees[i][0] and j[1] <= trees[i][1]:
                i_tl.append(j)

            if j[0] >= trees[i][0] and j[1] >= trees[i][1]:
                i_br.append(j)

            if j[0] >= trees[i][0] and j[1] <= trees[i][1]:
                i_bl.append(j)

    for j in range(4):
        if len(a[j]) != 0:
            print(trees[i], corners[j], sorted(a[j], key = lambda x: x[1]))

    print()


"""
5
1
2 4

15
8
4 7
4 1
14 11
10 6
13 4
4 10
10 3
9 14
"""