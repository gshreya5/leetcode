class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        for ind, i in enumerate(arr[::-1]):
            maxi = max(maxi, i)
            arr[len(arr) - ind - 1] = maxi

        return arr[1:] + [-1]

