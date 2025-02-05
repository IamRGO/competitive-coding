people = int(input())

weeks = []
column = []
possible = []

for i in range(people):
    weeks.append(list(input()))

for i in range(5):
    line = []
    for j in range(people):
        line.append(weeks[j][i])
    column.append(line)

for i in range(5):
    column[i] = column[i].count("Y")    


for i in range(len(column)):
    if column[i] == max(column):
        possible.append(i + 1)

possible = str(possible).strip("[]")
possible = possible.replace(" ", "")

print(possible)