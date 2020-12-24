#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans=[]
        i,j=0,1
        for a in A:
            if a%2==0:
                ans.insert(i,a)
                i=i+2
            else:
                ans.insert(j,a)
                j=j+2
        return ans
# @lc code=end

