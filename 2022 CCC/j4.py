"""
together = []
separate = []
vio = 0

x = int(input())
for i in range(x):
    a = input().split()
    a.sort()
    together.append(a[0] + " " + a[1])

y = int(input())
for i in range(y):
    b = input().split()
    b.sort()
    separate.append(b[0] + " " + b[1])

combo = {}

g = int(input())
for i in range(g):
    team = input().split()
    team.sort()
    combo[team[0] + " " + team[1]] = i
    combo[team[1] + " " + team[2]] = i
    combo[team[0] + " " + team[2]] = i

for term in together:
    if term not in combo:
        vio += 1
for term in separate:
    if term in combo:
        vio += 1

print(vio)
"""


together = []
seperate = []
teams = {}
vio = 0

t = int(input())
for i in range(t):
    together.append(" ".join(sorted(input().split())))

s = int(input())
for i in range(s):
    seperate.append(" ".join(sorted(input().split())))

a = int(input())
for i in range(a):
    group = sorted(input().split())
    teams[group[0] + " " + group[1]] = i
    teams[group[1] + " " + group[2]] = i
    teams[group[0] + " " + group[2]] = i

for i in together:
    if i not in teams:
        vio += 1

for i in seperate:
    if i in teams:
        vio += 1

print(vio)