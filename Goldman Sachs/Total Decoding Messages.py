# Question-8

# A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# You are an FBI agent. You have to determine the total number of ways that message can be decoded, 
# as the answer can be large return the answer modulo 109 + 7.

#Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 
# to 9 and If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.


class Solution:
	def CountWays(self, str):
		# Code starts here
        if str == '0' or str[0] == '0' or '00' in str:
            return 0
        n = len(str)    
        if n<=1:
            return 1        
            
        dp = [1 for _ in range(n+1)]  
    
        for i in range(2,n+1):
            (c1,c2) = (int(str[i-2]),int(str[i-1]))        
            if c1>0 and c2>0:
                if c1*10+c2 < 27:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                if c1 == 0:
                    dp[i] = dp[i-1]
                else:
                    if c1 > 2:
                        return 0
                    else:
                        dp[i] = dp[i-2]
        return dp[-1]%(10**9 + 7)
        # Code ends here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.CountWays(str)
		print(ans)

# } Driver Code Ends