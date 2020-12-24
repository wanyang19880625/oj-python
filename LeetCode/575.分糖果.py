#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)),len(candies)//2)
# @lc code=end

