#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        m=len(nums)
        for i in range(0,m-k+1):
            ans.append(max(nums[i:i+k]))
        return ans
# @lc code=end

