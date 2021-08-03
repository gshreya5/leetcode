class Solution:
    def isValid(self, s: str):

        if s.count('(') == s.count(')') and s.count('{') == s.count('}') and s.count('[') == s.count(']'):
            c = 0
            news = s
            while c < len(s):
                news = news.replace("()", "").replace("{}", "").replace("[]", "")
                c += 1
            if len(news) == 0:
                return True
            else:
                return False
        else:
            return False
