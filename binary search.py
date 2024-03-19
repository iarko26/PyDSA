#iterative binary search
def binarysearch(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(high+low)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
# l=[10,20,30,40,50,60,70,80,90,100]
l=[10,20,30,40,50]
x=25
if binarysearch(l,x)==-1:
    print("Element not found")
else:
    print("Element found at index",binarysearch(l,x))




        

