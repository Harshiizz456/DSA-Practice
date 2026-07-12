class Solution:
    def maxSubArray(self, nums):
        """ Problem: Maximum Subarray (Kadane's Algorithm)
        
        Approach:
        - Keep adding elements to current sum
        - If current sum becomes negative, reset it to 0
        - Track maximum sum at each step
        
        Time Complexity: O(n)
        Space Complexity: O(1) """
        total = 0
        maxi = float("-inf")

        for num in nums:
            total += num
            maxi = max(maxi, total)
            if total < 0:
                total = 0
        
        return maxi

