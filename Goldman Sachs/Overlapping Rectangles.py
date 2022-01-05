# Question-2

#Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates
#of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered 
#overlapping. (L1 and R1 are the extreme points of the first rectangle & L2 and R2 are the extreme points of the second rectangle).

class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
        #code starts here
        #diagram is given in the question, we can think of conditions where 
        #rectangles do not overap which is easier in general than other way
        #by genralising the given diagram 
        if L1[0] > R2[0] or L2[0] > R1[0] or L1[1] < R2[1] or L2[1] < R1[1]:
            return 0
        else:
            return 1
        #code ends here    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        p=[0]*2
        q=[0]*2
        r=[0]*2
        s=[0]*2
        p[0],p[1],q[0],q[1],r[0],r[1],s[0],s[1]=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.doOverlap(p,q,r,s)
        print(ans)
# } Driver Code Ends