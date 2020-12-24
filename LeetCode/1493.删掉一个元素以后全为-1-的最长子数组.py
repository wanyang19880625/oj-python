#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        cnt=0
        mx=0
        for r in range(len(nums)):
            if nums[r]==0:
                cnt+=1
            while l<r and cnt>=2:
                if nums[l]==0:
                    cnt-=1
                l+=1
            mx=max(mx,r-l)
        # print (mx)
        return mx
# @lc code=end

