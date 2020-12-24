#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A=="" and A==B:
            return True
        length=len(A)
        for x in range(0,length):
            temp=A[x:length]+A[0:x]
            if temp==B:
                return True
        return False
# @lc code=end

