# Question-3

#Given an array of positive numbers, the task is to find the number of possible 
#contiguous subarrays having product less than a given number k.

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code starts here
        count = 0
        p = 1
        l = 0
        for r in range(0,n):
            p*=a[r]
            while(p>=k):
                p/=a[l]
                l+=1
            count+=1+(r-l)
        return count
        #code ends here


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends