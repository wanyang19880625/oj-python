#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        index=[e[0] for e in enumerate(nums) if e[1]%2==1]
        if len(index)<k:
            return 0
        count=0
        for i in range(1,len(index)-k+1):
            count+=()
        
# @lc code=end

