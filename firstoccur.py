# def firstindex(arr,x):
#     for i in range(len(arr)):
#         if arr[i]==x:
#             return i
#     return -1

# x=int(input("Enter the element to be searched: "))
# # arr=[1,10,10,10,20,20,40]
# arr=[10,10,10]
# print("First occurence of element is at index",firstindex(arr,x))

# more efficient 
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
x=int(input("Enter the element to be searched: "))
arr=[10,10,10]
n=len(arr)
print("First occurence of element is at index",firstoccur(arr,n,x))

    
    


    
