n = int(input())

best = 0

for i in range(n):
    score = (int(input()) * 5 - int(input()) * 3)
    if score > 40:
        best += 1

print(str(best) + "+" if best == n else best)