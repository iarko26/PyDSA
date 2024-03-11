def checkPal(str,s,e):
    if s==e:
        return True
    if str[s]!=str[e]:
        return False
    if s<e+1:

        return checkPal(str,s+1,e-1)
    return True
    
def isPal(str):
    n=len(str)
    
    if n==0:
        return True
    return checkPal(str,0,n-1)

str="kiak"
if isPal(str):
    print("Yes")
else:
    print("No")
    



