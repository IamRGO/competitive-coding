tiles = int(input())

top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

def merge(count, t, b):
    for i in range(tiles):
        if t[i] == b[i] and t[i] == 1 and (i+1) % 2 == 1:
            count -= 2

    return count

def reduce(line):
    count = line.count(1) * 3
    i = 0

    while i < len(line):
        if line[i] == 1:
            j = i + 1

            while j < len(line):
                if line[j] == 1:
                    count -= 2
                else:
                    break
                j += 1
            i = j
        i += 1

    return count

tape = reduce(top)
tape += reduce(bottom)
tape = merge(tape, top, bottom)
print(tape)


"""
7
0 0 1 1 0 1 0
0 0 1 0 1 0 0

7
0 0 1 1 1 1 0
0 0 1 0 1 0 0

5
1 0 1 0 1
0 0 0 0 0

"""