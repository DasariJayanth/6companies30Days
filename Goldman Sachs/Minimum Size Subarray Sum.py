# Question-14

# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl,
# numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        s, min_len = 0, float('inf')
        while r <n:
            s += nums[r]
            while s >= target:
                min_len = min(min_len, r-l+1)
                s -= nums[l]
                l +=1
            r +=1
        return min_len if min_len != float('inf') else 0