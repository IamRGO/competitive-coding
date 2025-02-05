"""
chord = str(input())

change = []
for i in range(len(chord)):
    if chord[i] == "+":
        change.append(" tighten ")
        continue
    elif chord[i] == "-":
        change.append(" loosen ")
        continue
    change.append(chord[i])
    
change.append("end")
new = []
line = ""
j = -1
while j < len(change) - 1:

    j += 1
    if change[j].isdigit() == True:

        while j < len(change):
            if change[j].isdigit() == False:
                new.append([line])
                line = ""
                break
            line += change[j]
            j += 1
        
    line += change[j]

yikes = ""
for i in new:
    if new.index(i) == len(new) - 1:
        yikes += i[0]
        break
    yikes += i[0] + "\n"

print(yikes)
"""

tune = list(input())

clean = []
line = []

i = 0
while i < len(tune):
    if i == len(tune) - 1:
        clean.append(line)

    if tune[i].isalpha() == True:
        line.append(tune[i])

    if tune[i] == "+" or tune[i] == "-":
        line.append(" tighten " if tune[i] == "+" else " loosen ")

        j = i + 1
        while j < len(tune):
            if tune[j].isdigit() == True:
                line.append(tune[j])
            else:
                clean.append(line)
                line = []
                i = j - 1
                break

            j += 1
        
    i += 1

for i in clean:
    print("".join(i))
