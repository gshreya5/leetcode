class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()

        for i in nums2:
            if i in nums1:
                nums1.remove(i)
                res.add(i)
        return res
