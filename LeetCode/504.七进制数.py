#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        n=abs(num)
        ans=""
        while n>0:
            ans+=str(n%7)
            n=(int)(n/7)
        return ans[::-1] if num>=0 else "-"+ans[::-1]
# @lc code=end

