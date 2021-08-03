class Solution:
    def plusOne(self, digits: List[int]):
        st = ""
        for i in digits:
            st += str(i)
        i = int(st) + 1
        return list(str(i))


