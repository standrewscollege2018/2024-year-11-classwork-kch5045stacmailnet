H,W,N = input().split()
N = int(N)
spread = 0
totalspread = 0
for i in range(N):
    x, y, reach, colour = input().split(" ")
    reach = int(reach)
    if reach > 0:
        spread = ((int(reach)*2)+1)
        spread2 = spread**2
        x = int(x)+1
        y = int(y)+1
        if x == int(W):
            spread3 = spread2 - (spread*reach)
            if y == int(H):
                spread3 = spread2 - spread
                totalspread = totalspread + spread3
            else:
                totalspread = spread3
        elif y == int(H):
                spread3 = spread2 - spread*reach
                totalspread = totalspread + spread3
        else:
            totalspread = spread2
input()
print(totalspread)
