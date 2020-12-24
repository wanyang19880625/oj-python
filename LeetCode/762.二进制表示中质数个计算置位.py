#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
import math
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count=0
        def isPrime(n):
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    return False
            return True
        for num in range(L,R+1):
            bit=bin(num).count("1")
            if isPrime(bit) and bit>1:
                count+=1
        return count
# @lc code=end

