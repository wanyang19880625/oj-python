#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element=collections.Counter(nums)
        return [x for x in element.keys() if element.get(x)*3>len(nums)]
# @lc code=end

