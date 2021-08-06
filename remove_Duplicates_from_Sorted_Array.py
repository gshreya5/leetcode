class Solution:
    def removeDuplicates(self, nums: List[int]):
        if len(nums) == 0:
            return 0

        i = 0
        l = nums[-1]
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

# class Solution:
#     def removeDuplicates(self, nums: List[int]):
#         if not nums:
#             return 0
#         prev = nums[0]
#         minus = 0
#
#         for i, x in enumerate(nums[1:]):
#             i = i + 1
#             if x == prev:
#                 nums.remove(x)
#                 minus += 1
#             else:
#                 prev = nums[i - minus]
#
#         return len(nums)