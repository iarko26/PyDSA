def recbinary(l,x,low,high):
    if low>high:
        return -1
    if low<=high:
        mid=(low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            return recbinary(l,x,mid+1,high)
        else:
            return recbinary(l,x,low,mid-1)
    
def binarysearch(l,x):
    return recbinary(l,x,0,len(l)-1)

l=[10,20,30,40,50]
x=50
if binarysearch(l,x)==-1:
    print("Element not found")
else:
    print("Element found at index",binarysearch(l,x));
    
