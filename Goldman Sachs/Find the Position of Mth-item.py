# Question-7

# M items are to be delivered in a circle of size N. Find the position where the M-th item will be delivered if we start from 
# a given position K. Note that items are distributed at adjacent positions starting from K.

class Solution:
    def findPosition(self, N , M , K):
        # code starts here
        
        #  n- k + 1 is number of positions, before we reach beginning of circle
        if M<=N-K+1:               
            return M+K-1
        M = M-(N-K+1)
        # compute m % n to skip all complete rounds. 
        if M%N == 0:
            return N
        else:
            return M%N
        # code ends here    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M,K=map(int,input().split())
        
        ob = Solution()
        print(ob.findPosition(N,M,K))
# } Driver Code Ends