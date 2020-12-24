#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        m,cnt=1,1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i] :
                cnt+=1
            else :
                m=max(cnt,m)
                cnt=1
        return max(cnt,m)
# @lc code=end

