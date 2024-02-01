import math
def factorial(n):
    if n==0:
        return 0
    if n<1:
        return 1
    digit=0
    for i in range(2,n+1):
        digit=digit+math.log10(i)
    return math.floor(digit)+1
    
    
n=120
result=factorial(n)
print(result)
