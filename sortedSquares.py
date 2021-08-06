class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        start = 0
        end = len(nums) - 1
        index = end
        while start <= end:
            if nums[start] ** 2 <= nums[end] ** 2:
                res[index] = nums[end] ** 2
                end -= 1
            else:
                res[index] = nums[start] ** 2
                start += 1

            index -= 1
        return res


