class Solution:
    def my_pow(self, x: float, n: int) -> float:
        """递归"""
        if n < 0:
            return 1/(self.my_pow(x, -n))
        if n == 0:
            return 1

        t = self.my_pow(n//2)

        return t*t*x  if n % 2 else t*t

    def my_pow1(self, x: float, n: int) -> float:
        """二进制"""
        if x==0.0: return 0.0
        ans = 1
        if n < 0: x, n = 1/x, -n
        while n > 0:
            if n & 1: ans *= x
            x *= x
            n >>= 1
        return ans

    def my_pow2(self, x: float, n: int) -> float:
        """递归"""
        def quick_mul(n):
            if n == 0:
                return 1
            y = quick_mul(n>>1)
            return y*y*x if n&1 else y*y
        return quick_mul(n) if n >=0 else 1/quick_mul(-n)





