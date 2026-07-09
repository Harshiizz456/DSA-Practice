class Solution:
    def largest(self, arr):
        # code here
        largest_num = arr[0]
        for element in arr:
            if element > largest_num:
                largest_num = element
        return largest_num
            
