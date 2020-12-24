#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
import functools
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words==sorted(words,key=lambda w: [order.index(x) for x in w])

# @lc code=end

