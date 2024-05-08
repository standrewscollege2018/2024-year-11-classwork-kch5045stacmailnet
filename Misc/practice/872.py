#GCEPLS
ask = 0
G = 0
C = 0
E = 0
P = 0
L = 0
S = 0

inp = input()
while inp != "D":
    whatTea, numOfTea = inp.split()
    numOfTea = int(numOfTea)
    if  whatTea == "G":
        G = G + numOfTea
    elif whatTea == "C":
        C = C + numOfTea
    elif whatTea == "E":
        E = E + numOfTea
    elif whatTea == "P":
        P = P + numOfTea
    elif whatTea == "L":
        L = L + numOfTea
    elif whatTea == "S":
        S = S + numOfTea
    inp = input()

print(f"{G} {C} {E} {P} {L} {S}")
"""
tea = []
    te = input()
    tea.append(te)
    num_of_tea = int(input())
    tea.append(num_of_tea)"""
