
class Solution:

    def remove_duplicates(self, nums):
        i = 0 
        for j in range(len(nums):
            if nums[i] < nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1


