#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==0:
            return 0
        l,r=0,max(citations)
        def check(m):
            count=0
            for c in citations:
                if c>=m:
                    count+=1
            return count<=m
        while l<r:
            mid=(l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return l
# @lc code=end

