from typing import List


class Solution:
    def group_anagrams(self, strs:List[str])->List[List[str]]:
        """sort+hash O(NKlogk)"""
        d = {}
        for s in strs:
            k = "".join(sorted(s))
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]
        return [d[k] for k in d]

    def group_anagrams(self, strs:List[str])->List[List[str]]:
        """count+hash O(Nk)"""
        d = {}
        for s in strs:
            li = [0] * 26
            for i in s:
                li[ord(i)-97] += 1
            k = tuple(li)
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]
        return [d[k] for k in d]






