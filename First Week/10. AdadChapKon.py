x = input()
mylist = list()

# for _ in range(len(str(x))):
#     mylist.append(x%10)
#     x = x//10

for d in str(x):
    mylist.append(int(d)) 
    
# mylist.reverse()
for i in mylist:
    print(f"{i}: {i*str(i)}")