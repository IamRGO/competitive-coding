n = int(input())
tree_count = int(input())

tree_list = [
    [-1, -1]
]

tree_hash = {}

for i in range(tree_count):
    t = list(map(int, input().split()))
    tree_list.append(t)

    if t[0] not in tree_hash:
        tree_hash[t[0]] = []
    tree_hash[t[0]].append(t[1])

def contains_tree(pool):
    t, b, l, r = pool
    for tree in tree_list:
        if (
            tree[1] >= l and tree[1] <= r and
            tree[0] >= t and tree[0] <= b
        ):
            return True
    return False

y_trees = sorted(list(tree_hash.keys()))
best = 1

for tree in tree_list:
    bottom = 0
    right = 0

    if tree[0] in y_trees:
        bottom = y_trees.index(tree[0])
    else:
        bottom = y_trees[0]

    if tree[1] in tree_hash[bottom]:
        right = tree_hash[bottom].index(tree[1])
    else:
        right = sorted(tree_hash[bottom])[0]
    
    size = min(bottom - tree[0], right - tree[1])

    if size > best:
        best = size

print(best)

