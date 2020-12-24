#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return "".join(sorted([str(x) for x in nums],reverse=True))
# @lc code=end

