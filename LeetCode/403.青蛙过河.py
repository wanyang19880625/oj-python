#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        k=1
        dp=[False]*len(stones)
        dp[0]=True
        for i in range(1,len(stones)):
            

# @lc code=end

