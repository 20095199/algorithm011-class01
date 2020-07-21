from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """暴力"""
        rst = []

        def generate(li):
            if len(li) == 2*n:
                if valid(li):
                    rst.append("".join(li))
                return
            li.append('(')
            generate(li)
            li.pop()
            li.append(')')
            generate(li)
            li.pop()

        def valid(li):
            bal = 0
            for s in li:
                if s == "(":
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        generate([])
        return rst

    def generateParenthesis2(self, n: int) -> List[str]:
        """回朔, 不过我确实没感觉到哪里体现了回朔"""
        rst = []

        def generate(li, left, right):
            if len(li) == 2*n:
                rst.append("".join(li))
            if left < n:
                li.append("(")
                generate(li, left+1, right)
                li.pop()
            if right < left:
                li.append(")")
                generate(li, left, right+1)
                li.pop()
        generate([], 0, 0)
        return rst

    def generateParenthesis3(self, n: int) -> List[str]:
        """dfs, 这才有点回朔的意思"""
        rst = []

        def dfs(s, left, right):
            if left == n and right == n:
                rst.append(s)
                return
            if right > left:
                return 
            if left < n:
                dfs(s+"(", left+1, right)
            if right < n:
                dfs(s+")", left, right+1)
        dfs("", 0, 0)
        return rst

    def generateParenthesis2(self, n: int) -> List[str]:
        """dfs, 这才有点回朔的意思"""
        rst = []

        def dfs(s, left, right):
            if left == n and right == n:
                rst.append(s)
                return
            if left < n:
                dfs(s+"(", left+1, right)
            if right < left:
                dfs(s+")", left, right+1)
        dfs("", 0, 0)
        return rst
            


            

                    

