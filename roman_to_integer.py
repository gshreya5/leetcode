class Solution:

    def romanToInt(self, a):
        total = 0
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = dic[a[-1]]
        for i in a[::-1]:
            if dic[i] >= prev:
                total += dic[i]
            else:
                total -= dic[i]

            prev = dic[i]

        return total


