pie = int(input())
people = int(input())
# pie = 6
# people = None

line = []
l_hist = []
def search(combo, hist):
    # print(combo)
    if hist in l_hist:
        return

    if pie == people:
        line.append([0])
        return

    if people == 1:
        line.append([0])
        return

    if len(combo) == people and sum(combo) == pie:
        line.append(combo)
        # print(hist + [combo], "from", people)
        l_hist.append(hist + [combo])

    else:
        for i in range(1, pie + 1):
            next = sorted(list(combo) + [i])
            if (next in line):
                continue
            
            if len(next) >= people and sum(next) < pie:
                continue

            if len(next) < people and sum(next) == pie:
                continue
            
            if sum(next) > pie:
                break

            else:
                search(next, hist + [combo])

    return

# for i in range(pie):
#     line = []
#     people = i + 1
search([], [])
    # print(line)
print(len(line))

"""
250
50

27
3

8
4

6
2
"""