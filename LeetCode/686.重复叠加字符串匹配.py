#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#

# @lc code=start
import string
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        a=len(A)
        b=len(B)
        if a>b:
            if A.find(B)>-1:
                return 1
            if (2*A).find(B)>-1:
                return 2
            else:
                return -1
        ans=1
        repeated=A
        while len(repeated)<=b*2 :
            if repeated.find(B)>-1:
                return ans
            repeated+=A
            ans+=1
        return ans if repeated.find(B)>-1 else -1
# @lc code=end

