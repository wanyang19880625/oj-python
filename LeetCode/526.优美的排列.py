#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#

# @lc code=start
class Solution:
    count=0
    def countArrangement(self, N: int) -> int:
        v=[False]*(N+1)
        def dfs(start):
            if start>N:
                self.count+=1
            for i in range(1,N+1):
                if v[i]==False and (i%start==0 or start%i==0):
                    v[i]=True
                    dfs(start+1)
                    v[i]=False
        dfs(1)
        return self.count
# @lc code=end

