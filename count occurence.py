def firstoccur(arr,n,x):
    low =0
    high = n-1
    while low<=high:
        mid=(low+high)//2
        if x>arr[mid]:
            low=mid+1
        elif x<arr[mid]:
            high=mid-1
        else:
            if mid==0 or arr[mid-1]!=arr[mid]:
                return mid
            else:
                high=mid-1
    return -1
def lastoccur(arr,n,x):
    low =0
    high=n-1
    while low<=high:  
        mid=(low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            if mid==n-1 or arr[mid]!=arr[mid+1]:
                return mid
            else:
                low=mid+1
    return -1
def countoccur(arr,n,x):
    first=firstoccur(arr,n,x)
    if first==-1:
        return 0
    else:
        last=lastoccur(arr,n,x)-first+1
        return last
        
    
arr=[10,10,10,20,20,40]
n=len(arr)
x=10
print("Count of element is",countoccur(arr,n,x))