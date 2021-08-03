class Solution:
    def removeDuplicates(self, nums: List[int]):
        if not nums:
            return 0
        prev = nums[0]
        minus = 0

        for i, x in enumerate(nums[1:]):
            i = i + 1
            if x == prev:
                nums.remove(x)
                minus += 1
            else:
                prev = nums[i - minus]

        return len(nums)

