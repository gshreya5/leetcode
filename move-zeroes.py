class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        c = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            else:
                c += 1
        nums[:] = nums[:i] + c * [0]

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in nums:
#             if i == 0:
#                 nums.remove(i)
#                 nums.append(i)
#
#         return nums
