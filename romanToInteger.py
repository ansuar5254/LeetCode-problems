I,V,X,L,C,D,M = 1,5,10,50,100,500,1000
S = "MCMXCIV"
result = []
for i in S:
    if i == 'I':
        result.append(1)
    elif i == 'V':
        result.append(5)
    elif i == 'X':
        result.append(10)
    elif i == 'L':
        result.append(50)
    elif i == 'C':
        result.append(100)
    elif i == 'D':
        result.append(500)
    elif i == 'M':
        result.append(1000)
fina = 0
if result[0] >= result[1]:
    fina =result[0] + result[1]
else:
    fina = result[1]-result[0]   
for i in range(len(result)-2):
    if result[i+1] >= result[i+2]:
        fina += result[i+2]
    else:
        fina +=(result[i+2] - 2*result[i+1])
print(fina)
    
    

    
