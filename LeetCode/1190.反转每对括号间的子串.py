#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        temp=""
        for i in range(len(s)):
            if s[i]!='(' and s[i]!=')':
                temp+=s[i]
            if s[i]=='(' and temp!="":
                stack.append(temp)
                temp=""
            if s[i]==')' or i==len(s)-1:
                if len(stack)>0:
                    top=stack.pop()
                    temp=top+temp[::-1]
                else:
                    stack.append(temp)
# @lc code=end

