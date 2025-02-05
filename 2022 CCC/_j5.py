n = int(input())
tree_count = int(input())

tree_list = []

for i in range(tree_count):
    t = list(map(int, input().split()))
    tree_list.append(t)

tree_list_y_sorted = tree_list.copy()
tree_list_y_sorted.sort(key = lambda tree: tree[0])

tree_list_x_sorted = tree_list.copy()
tree_list_x_sorted.sort(key = lambda tree: tree[1])

def contains_tree(pool):
    t, b, l, r = pool
    for tree in tree_list:
        if (
            tree[1] >= l and tree[1] <= r and
            tree[0] >= t and tree[0] <= b
        ):
            return True
    return False

biggest_pool = 1

possible_pools = [
    # [1, n, 1, n] # top bottom left right
    [100, n, 100, n]
]

while len(possible_pools) > 0:
    print(len(possible_pools))
    next_possible_pools = []
    for pool in possible_pools:
        if contains_tree(pool) == False:
            t, b, l, r = pool
            width = r - l
            height = b - t
            size = min(width, height) + 1

            if size > biggest_pool:
                print("WE HAVE FOUND A POOL", size)
                biggest_pool = size
        else:
            top, bottom, left, right = pool
            # move the top wall
            for tree in tree_list_y_sorted:
                if (
                    tree[1] >= left and tree[1] <= right and
                    tree[0] >= top and tree[0] <= bottom
                ):
                    if tree[0] + 1 < n:
                        next_possible_pools.append(
                            [tree[0] + 1, bottom, left, right]
                        )
                    break
            # move the left wall
            for tree in tree_list_x_sorted:
                if (
                    tree[1] >= left and tree[1] <= right and
                    tree[0] >= top and tree[0] <= bottom
                ):
                    if tree[1] + 1 < n:
                        next_possible_pools.append(
                            [top, bottom, tree[1] + 1, right]
                        )
                    break
            # move the bottom wall
            for tree in reversed(tree_list_y_sorted):
                if (
                    tree[1] >= left and tree[1] <= right and
                    tree[0] >= top and tree[0] <= bottom
                ):
                    if tree[0] - 1 > 0:
                        next_possible_pools.append(
                            [top, tree[0] - 1, left, right]
                        )
                    break
            # move the right wall
            for tree in reversed(tree_list_x_sorted):
                if (
                    tree[1] >= left and tree[1] <= right and
                    tree[0] >= top and tree[0] <= bottom 
                ):
                    if tree[1] - 1 > 0:
                        next_possible_pools.append(
                            [top, bottom, left, tree[1] - 1]
                        )
                    break
    possible_pools = next_possible_pools
                    
print(biggest_pool)