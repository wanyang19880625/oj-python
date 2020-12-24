#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start,end=0,0
        ans=[]
        if len(nums)==0:
            return ans
        for i in range(0,len(nums)-1):
            if nums[i]+1!=nums[i+1]:
                if start==end:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start])+"->"+str(nums[end]))
                start=i+1
            end=i+1
        if start==end:
            ans.append(str(nums[start]))
        else:
            ans.append(str(nums[start])+"->"+str(nums[end]))
        return ans
# @lc code=end

