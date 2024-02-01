# def isprime(n):
#     if n==1:
#         return False
#     i=2
#     while(i*i<=n):
#         if n%i==0:
#             return False
#         i+=1
#     return True

# n=int(input("enter number:"))

# if isprime(n):
#     print("True")
# else:
#     print("False")

# super effiecint
def isprime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5;
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True
n=int(input("enter the number:"))
if isprime(n):
    print("True")
else:
    print("False")
