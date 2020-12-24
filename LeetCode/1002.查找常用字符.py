#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        intersection=[set(A[x])&set(A[x+1]) for x in range(0,len(A)-1)][-1]
        l=[min([(x,t.count(x)) for t in A]) for x in intersection]
        ans=[]
        for x in l:
            ans+=x[0]*x[1]
        return ans
# @lc code=end

