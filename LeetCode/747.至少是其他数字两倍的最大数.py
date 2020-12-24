#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        m=sorted(nums)
        return list(nums).index(m[-1]) if m[-1]>=m[-2]*2 else -1

# @lc code=end

