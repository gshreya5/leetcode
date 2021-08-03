class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        res = []

        for i in nums:
            if i != val:
                count += 1
                res.append(i)
        nums[:] = res
        return count

