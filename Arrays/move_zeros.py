class Solution:
    def moveZeroes(self, nums):
        
      """Problem: Move Zeros
        Move all 0's to the end while maintaining order of non-zero elements
        
        Time Complexity: O(n)
        Space Complexity: O(1) """
        
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
