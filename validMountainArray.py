class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        j = 0
        c = 0
        while j < len(arr) - 1:
            if arr[j + 1] > arr[j]:
                j += 1
                c = 1
            else:
                break
        if c == 1:
            while j < len(arr) - 1:
                if arr[j + 1] < arr[j]:
                    j += 1
                    c = 2
                else:
                    return False
        return c == 2


