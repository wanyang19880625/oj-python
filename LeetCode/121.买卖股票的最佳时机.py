#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        dp=[0]*len(prices)
        mn=prices[0]
        for i in range(1,len(prices)):
            mn=min(mn,prices[i])
            dp[i]=max(prices[i]-mn,dp[i])
        return max(dp)
# @lc code=end

