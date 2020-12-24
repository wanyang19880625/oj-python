#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
import collections
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d=dict(collections.Counter(nums))
        ans=[]
        error=[k for k in d.keys() if d[k]>1]
        ans.append(error[0])
        ans.append(-sum(nums)+error[0]+int((len(nums)+1)*len(nums)/2))
        return ans
# @lc code=end

