class Solution:
    def heightChecker(self, heights: List[int]):
        op = 0
        for index, height in enumerate(sorted(heights)):
            if height != heights[index]:
                op+=1
        return op