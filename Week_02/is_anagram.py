
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





