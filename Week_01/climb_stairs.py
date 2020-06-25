
class Solution:

    def climb_stairs(self, n):
        if n < 3:
            return n
        f1, f2 = 1, 2
        for f in range(3, n+1):
            f1, f2 = f2, f1+f2
        return f2

