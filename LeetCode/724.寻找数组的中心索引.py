#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0
        prefix=[0]
        for i in range(0,len(nums)):
            prefix.append(prefix[i]+nums[i])
        # print (prefix)
        for i in range(1,len(nums)+1):
            if prefix[i-1]==prefix[len(nums)]-prefix[i]:
                return i-1
        return -1
# @lc code=end

