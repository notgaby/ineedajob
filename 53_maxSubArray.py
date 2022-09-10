#https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = tempSum = nums[0]
        
        for num in nums[1:]:
            tempSum = max(num, tempSum + num)
            maxSum = max(maxSum, tempSum)
        return maxSum
            
        
