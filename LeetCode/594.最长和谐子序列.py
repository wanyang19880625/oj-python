#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d=dict()
        for n in nums:
            d[n]=d.setdefault(n,0)+1
        ans=0
        for n in nums:
            ans=max(d[n]+d[n-1] if (n-1) in d.keys() else 0,
                d[n]+d[n+1] if (n+1) in d.keys() else 0,ans)
        return ans
# @lc code=end

