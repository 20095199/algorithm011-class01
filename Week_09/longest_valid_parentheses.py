
class Solution:

    def longestValidParentheses(self, s: str) -> int:

        ans=0     
        stack=[-1,]
        for i,ch in enumerate(s):
            if '('==ch: 
                stack.append(i)
            elif len(stack)>1:  
                stack.pop()    
                ans = max(ans, i - stack[-1])
            else:  
                stack[0]=i
        return ans
