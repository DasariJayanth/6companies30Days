# Question-15

# Given an array of integers and a number k, write a function that returns true 
# if given array can be divided into pairs such that sum of every pair is divisible by k.

#User function Template for python3
from collections import defaultdict

class Solution:
	def canPair(self, nums, k):
		# Code starts here

        # An odd length array cannot be divided into pairs
		if len(nums) & 1:
		    return 0
        # Create a frequency array to count occurrences of all remainders when divided by k.    
		freq = defaultdict(lambda: 0) 
        # Count occurrences of all remainders
		for i in range(0, n):
            freq[((nums[i] % k) + k) % k] += 1
        # Traverse input array and use freq[] to decide if given array can be divided in pairs.    
		for i in range(0, n):
        # Remainder of current element
            rem = ((nums[i] % k) + k) % k
        # If remainder with current element divides k into two halves.
            if (2 * rem == k):
                # Then there must be even occurrences of such remainder
                if (freq[rem] % 2 != 0):
                    return 0
        # If remainder is 0, then there must be two elements with 0 remainde
            elif (rem == 0):
                if (freq[rem] & 1):
                    return 0
            # Else number of occurrences of remainder must be equal to
            # number of occurrences of k - remainder
            elif (freq[rem] != freq[k - rem]):
                return 0
        return 1        
		# Code ends here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends