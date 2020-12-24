#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m=sorted(intervals,key=lambda x:x[0])
        ans=[]
        for i in range(0,len(m)):
            if len(ans)==0 or m[i][0]>ans[-1][1]:
                ans.append(m[i])
                continue
            if m[i][0]>=ans[-1][0] and m[i][0]<=ans[-1][1]:
                ans[-1][1]=max(m[i][1],ans[-1][1])
        return ans
# @lc code=end

