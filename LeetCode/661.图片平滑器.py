#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in len(M):
            for j in len(M[i]):
                if i==0 and j==0:
                    ans.append()                    

# @lc code=end

