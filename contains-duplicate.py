class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        a = list(set(nums))
        a.sort()
        return not nums == a

