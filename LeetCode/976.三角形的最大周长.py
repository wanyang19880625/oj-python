#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        ans=0
        sort=sorted(A,reverse=True)
        l=[(sort[i],sort[i+1],sort[i+2]) for i in range(0,len(sort)-2) if (sort[i+2]+sort[i+1]) >sort[i]]
        # print max([sum(num) for num in l])
        ans=[sum(num) for num in l]
        ans.append(0)
        return max(ans)
# @lc code=end

