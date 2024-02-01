class Solution:
    #You need to complete this function
    def factorial(self,N):
        if N==0:
            return 1
    
        
        return N*self.factorial(N-1)

if __name__ == "__main__":
    s=Solution()
    N=int(input("enter number:"))
    result1=s.factorial(N)
    print(result1)
