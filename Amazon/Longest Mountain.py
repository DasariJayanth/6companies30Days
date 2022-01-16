# Question-2

#ctrl+k,c  ====> multiple lines comment

# You may recall that an array arr is a mountain array if and only if:

# -> arr.length >= 3
# -> There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
#     -> arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#     -> arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        le = len(arr)
        z = 0
        if le<3:
            return z
        
        for i in range(1,le):
            l = 1 
            r=0
            #print(f"for value {i}")
            for j in range(i-1,-1,-1):
             #   print(f"{j}-->{arr[j]}")
                if arr[j+1]>arr[j]:
                    l +=1
                else:
                    break
            if l==1:
                l=0
                continue
            for k in range(i+1,le):
              #  print(f"{k}-->{arr[k]}")
                if arr[k-1]>arr[k]:
                    r=1
                    l +=1
                else:
                    break
            if l>1 and r==1:
                z = max(z,l)   
            #print(z)
        return z    