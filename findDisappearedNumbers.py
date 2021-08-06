class Solution:
    def findDisappearedNumbers(self, nums: List[int]):

        for i in nums:
            a = abs(i) - 1
            if nums[a] > 0:
                nums[a] *= -1

        return [x + 1 for x in range(len(nums)) if nums[x] > 0]










