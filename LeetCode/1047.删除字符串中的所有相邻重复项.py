#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=[]
        for x in list(S):
            if len(stack)==0 or stack[-1]!=x:
                stack.append(x)
            else:
                stack.pop()
        # print (stack)
        return "".join(stack)
# @lc code=end

