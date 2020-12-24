#
# @lc app=leetcode.cn id=1033 lang=python3
#
# [1033] 移动石子直到连续
#

# @lc code=start
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # list=[a,b,c]
        list=sorted([a,b,c])
        print (list)
        return [min(1,list[1]-list[0]-1)+min(1,list[2]-list[1]-1),
                max(list)-min(list)-2]
        
# @lc code=end

