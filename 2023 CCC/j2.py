SHU = {"Poblano" : 1500, "Mirasol" : 6000, "Serrano" : 15500,
       "Cayenne" : 40000, "Thai" : 75000, "Habanero" : 125000}

chili = 0
peppers = int(input())

for i in range(peppers):
    chili += SHU[input()]

print(chili)