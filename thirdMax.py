class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)

        a, b, c = sorted(nums[:3])

        for i in range(3, len(nums)):
            if nums[i] > c:
                a = b
                b = c
                c = nums[i]
            elif nums[i] > b:
                a = b
                b = nums[i]
            elif nums[i] > a:
                a = nums[i]

        return a









