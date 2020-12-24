#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
import collections
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m=dict(collections.Counter(moves))
        # print (m)
        return m.get('U',0)==m.get('D',0) and m.get('L',0)==m.get('R',0)
# @lc code=end

