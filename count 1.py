def count(arr,n):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if mid==n-1 or arr[mid+1]==0 and arr[mid]==1:
            return mid+1
        if arr[mid]==1:
            low=mid+1
        else:
            high=mid-1


    



            



    return -1
arr = [1, 1, 0, 0, 0, 0, 0]
n=len(arr)

print("Count of element is",count(arr,n))

            


        
    