x = input()
n = len(x)

# slising
xl = ""
xr = ""
for i in range(n):
    if i < n/2:
        xl += x[i]
    else:
        xr += x[i]

if n % 2 == 1:
    print("NO!")
else:
    if int(xr) > int(xl): 
        sum1 = int(xl)
        for _ in range(1, abs(int(xr)-int(xl))+1):
            sum1 += int(xl) + _
        if sum1 == int(x):
            print("YES!")
        else:
            print("NO!")  
    elif int(xl) > int(xr):
        sum2 = int(xr)
        for _ in range(1, abs(int(xr)-int(xl))+1):
            sum2 += int(xr) + _
        if sum2 == int(x):
            print("YES!")
        else:
            print("NO!")  
    else:
        print("NO!")

