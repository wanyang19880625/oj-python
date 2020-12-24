#
# @lc app=leetcode.cn id=849 lang=python3
#
# [849] 到最近的人的最大距离
#

# @lc code=start
import math
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDis=0
        index=seats.index(1)
        first=index
        for i in range(index,len(seats)):
            if seats[i]==1:
                maxDis=max(maxDis,math.floor((i-index)/2.0))
                index=i
        return max(first,maxDis,len(seats)-1-index)

# @lc code=end

