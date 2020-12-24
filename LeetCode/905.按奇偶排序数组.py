#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans=[]
        for a in A:
            if a%2==0:
                ans.insert(0,a)
            else:
                ans.append(a)
        return ans
# @lc code=end

