class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if 0 not in arr:
            return arr
        else:
            i = 0
            while i < len(arr) - 1:
                if arr[i] == 0:
                    arr[:] = arr[0:i + 1] + [0] + arr[i + 1:len(arr) - 1]
                    i += 2
                else:
                    i += 1


