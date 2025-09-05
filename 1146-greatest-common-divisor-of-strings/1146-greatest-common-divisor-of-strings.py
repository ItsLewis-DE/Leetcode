class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def ucln(a,b):
            if b==0:
                return a
            return ucln(b,a%b)
        len_kq = ucln(len(str1),len(str2))
        candidate = str1[:len_kq]
        if str1 == candidate * (len(str1)//len(candidate)) and str2 == candidate * (len(str2)//len(candidate)):
            return candidate
        return ""