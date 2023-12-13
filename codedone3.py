x = [int(x) for x in list(input().split(" "))]
y = [int(x) for x in list(input().split(" "))]

c = 0
for i in range(3):
    if (x[i] == 1) and (y[i] == 0):
        c += 1
    elif (x[i] == 0) and (y[i] == 1):
        c += 1

if c == 3:
    print("NO")
else:
    print("YES")
#BELLBELL