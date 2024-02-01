# def nond(arr,n):
#     count=0
#     n=len(arr)
    
#     for i in range(1,n):
        
#         if arr[i-1]>arr[i]:
#             count+=1
#             if count>1:
#                 return False
#             if arr[i+1]<arr[i] and arr[i+1]>arr[i-1]:
#                 arr[i+1]=arr[i]
#             else:
#                 arr[i]=arr[i-1]
            
            
                
            
            
                
            
#     return True
# # #test case 1
# arr = [4,8,7,9]
# n=len(arr)
# print("Number of times the array is modified:",nond(arr,n))

# #test case 2
# arr1=[4,8,7,3]
# m=len(arr1)
# print("Number of times the array is modified:",nond(arr1,m))


#another way
def isPossible(arr, n):
    # Write your code here.
    count=0
    n=len(arr)
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            count+=1
            if count>1:
                return False
            
            if i>1 and arr[i-2] >arr[i]:
                arr[i]=arr[i-1]
            else:
                arr[i-1]=arr[i]
    return True

arr=[7,
3,
8, 4, 6]
n=len(arr)
print("Is it possible to sort the given array? ",isPossible(arr,n))



            

                
                    

            
