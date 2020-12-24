#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
import copy
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def dfs(start,temp):
            c=temp.copy()
            if len(c)>=2 and c not in ans:
                ans.append(c)
            for i in range(start,len(nums)):
                if len(c)==0 or c[-1]<=nums[i]:
                    temp.append(nums[i])
                    dfs(i+1,temp)
                    temp.pop()
        dfs(0,[])
        return ans
# @lc code=end

