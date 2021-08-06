class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return nums

        i = 0
        odd = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[odd], nums[j] = nums[j], nums[odd]
                odd += 1
                i += 1
            else:
                nums[i] = nums[j]
                i += 1
        return nums

