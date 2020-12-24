#
# @lc app=leetcode.cn id=1073 lang=python3
#
# [1073] 负二进制数相加
#

# @lc code=start
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s1,s2=0,0
        for i in range(len(arr1[::-1])):
            if arr1[::-1][i]==1:
                s1+=(-2)**i
        for i in range(len(arr2[::-1])):
            if arr2[::-1][i]==1:
                s2+=(-2)**i
        s=s1+s2
        ans=[]
        if s==0:
            return [0]
        while s!=0:
            mod=s%-2
            s=s//-2
            if mod>=0:
                ans.append(mod)
            else:
                s+=1
                ans.append(1)
        return ans[::-1]
# @lc code=end

