
class Solution:
    
    def is_anagram(s: str, t: str)->bool:
        """hash表法"""
        if len(s) != len(t):
            return False

        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in t:
            if i not in d:
                return False
            d[i] -= 1
            if d[i] < 0:
                return False
        return True

    def is_anagram2(s:str, t:str)->bool:
        """hash映射"""
        array = [0]*26
        for i in s:
            array[ord(i)-97] += 1
        for i in t:
            array[ord(i)-97] -= 1
        return not any(array)

    def is_anagram3(s:str, t:str)->bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            d[t[i]] = d.get(t[i], 0) - 1
        for k in d:
            if d[k] < 0:
                return False
        return True






