


# Question-

# Given an unsorted array Arr of size N of positive integers. 
# One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

class Solution:
    def findTwoElement( self,arr, n): 
        # code starts here
        repeat = 0
        missing = 0
        for i in range(n):
            if arr[abs(arr[i])-1] < 0:
                repeat = abs(arr[i])                
            arr[abs(arr[i])-1] = -1 * abs(arr[abs(arr[i])-1])
        for i in range(n):
            if arr[i] > 0:
                missing = i+1     
                break
        return repeat, missing
        # code ends here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends