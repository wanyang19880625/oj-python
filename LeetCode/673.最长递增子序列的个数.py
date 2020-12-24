#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
import collections
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        count=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range (0,i):
                if nums[i]>nums[j]:
                    if dp[j]>=dp[i]:
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif dp[i]==dp[j]+1:
                        count[i]+=count[j]
        return sum([x for (i,x) in enumerate(count) if dp[i]==max(dp)])
# @lc code=end

