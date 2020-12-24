#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        index=[i for i in range(0,len(S)) if S[i]==C]
        ans=[min([abs(j-i) for j in index]) for i in range(0,len(S))]
        return ans
# @lc code=end

