#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        if len(v1)>len(v2):
            v2.extend([0]*(len(v1)-len(v2)))
        elif len(v1)<len(v2):
            v1.extend([0]*(len(v2)-len(v1)))
        for i in range(0,len(v1)):
            if int(v1[i])>int(v2[i]):
                return 1
            elif int(v1[i])<int(v2[i]):
                return -1
        return 0
# @lc code=end

