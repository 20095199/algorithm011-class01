
from typing import List

class Solution:

    def max_area(height:List[int])->int:
        i, j, m = 0, len(height)-1, 0
        while i < j:
            if height[i] < height[j]:
                m = max(height[i]*(j-i), m)
                i += 1
            else:
                m = max(height[j]*(j-i), m)
                j -= 1
        return m
