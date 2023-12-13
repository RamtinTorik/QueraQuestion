x = input()

n = len(x)
roman_numbers={'I':1 ,'V':5 ,'X':10 ,'L':50 ,'C':100 ,'D':500 ,'M':1000}
sum = 0

i = 0
while i<n:
    if i+1==n-1:
        if roman_numbers[x[i]] >= roman_numbers[x[i+1]]:
            sum += roman_numbers[x[i]] + roman_numbers[x[i+1]]
            i += 1
        else:
            sum += roman_numbers[x[i+1]] - roman_numbers[x[i]]
            i += 1
    else:
        if roman_numbers[x[i]] >= roman_numbers[x[i+1]]:
            sum += roman_numbers[x[i]]
        else:
            sum += roman_numbers[x[i+1]] - roman_numbers[x[i]]
            i += 1
    if i+1!=n-1:
        i += 1
    else:
        sum += roman_numbers[x[i+1]]
        break

            
print(sum)
            
            
            
            
            
        