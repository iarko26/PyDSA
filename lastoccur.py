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
x=int(input("Enter the element to be searched: "))
arr=[5, 10, 10, 10, 10, 20, 20]
n=len(arr)
print("Last occurence of element is at index",lastoccur(arr,n,x))


