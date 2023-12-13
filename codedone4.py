x = [int(i) for i in list(input().split(" "))]
# y = [int(i) for i in list(input().split(" "))]

dx = {}
# dy = {}

for i in x:
    if str(i) in dx.keys():
        dx[f"{i}"] += 1
    else:
        dx[f"{i}"] = 1
    
# for i in y:
#     if str(i) in dy.keys():
#         dy[f"{i}"] += 1
#     else:
#         dy[f"{i}"] = 1
sum = 0
print(dx)

for key in dx.keys():
    if int(key) == 0:
        sum += 1
    elif int(key) == dx.get(key)-1:
        sum += int(key)+1
    else:
        sum += (int(key))*2
        
print(sum)

# print("dx: ", dx)
# print("dy: ", dy)
