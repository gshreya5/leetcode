class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = {}

        for i in arr:
            if i in dic:
                return True
            else:
                if i % 2 == 0:
                    dic[i * 2] = i
                    dic[i / 2] = i
                else:
                    dic[i * 2] = i
        return False