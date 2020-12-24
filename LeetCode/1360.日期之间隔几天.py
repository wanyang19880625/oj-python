#
# @lc app=leetcode.cn id=1360 lang=python3
#
# [1360] 日期之间隔几天
#

# @lc code=start
from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        ymd1=date1.split('-')
        ymd2=date2.split('-')
        print(ymd1)
        print(ymd2)
        start=date((int)(ymd1[0]),int(ymd1[1]),int(ymd1[2]))
        end=date((int)(ymd2[0]),(int)(ymd2[1]),int(ymd2[2]))
        return abs((end-start).days)
# @lc code=end

