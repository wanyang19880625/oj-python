#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        n=sum([b[x]*(10**(len(b)-x-1)) for x in range(len(b)-1,-1,-1)])
        # print (n)
        res = 1
        while(n):
            if (n&1):
                res = (res*a) % 1337
            n >>= 1
            a = (a*a) % 1337
        return res
# @lc code=end

