#
# @lc app=leetcode.cn id=1328 lang=python3
#
# [1328] 破坏回文串
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)<=1:
            return ""
        mid=len(palindrome)//2
        index=0
        while index<mid:
            if palindrome[index]!='a':
                return palindrome[:index]+'a'+palindrome[index+1:]
            index+=1
        return palindrome[:len(palindrome)-1]+'b'
            
# @lc code=end

