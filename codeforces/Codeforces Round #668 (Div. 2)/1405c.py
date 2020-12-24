# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-09-07 23:34
# @url:https://codeforc.es/contest/1405/problem/C
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,os
from io import BytesIO, IOBase
import collections,itertools,bisect,heapq,math,string
from decimal import *
# region fastio

BUFSIZE = 8192

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# ------------------------------
## 注意嵌套括号!!!!!!
## 先有思路,再写代码,别着急!!!
## 先有朴素解法,不要有思维定式,试着换思路解决
def main():
    t=int(input())
    for i in range(t):
        n,k=map(int,input().split())
        ss=str(input())
        cnt=[0]*3
        # init s,s[j]一定等于s[j+k],其中一个问号的字符=另一个非问号
        s=list(ss)
        for j in range(0,n-k):
            if s[j]!='?' and s[j+k]=='?':
                s[j+k]=s[j]
            if s[j]=='?' and s[j+k]!='?':
                s[j]=s[j+k]
        ## sliding window
        l,dis=0,0
        f=True
        while l<=n-k:
            while dis<k:
                if s[l+dis]=='0':
                    cnt[0]+=1
                elif s[l+dis]=='1':
                    cnt[1]+=1
                else:
                    cnt[2]+=1
                dis+=1
            # '?'的count如果小于1和0的差值必然不能平衡
            # consecutive two string's head must be equal to tail if both head and tail not equal '?',otherwise is not balanced
            if cnt[2]<abs(cnt[1]-cnt[0]) or (l+k<n and s[l]!=s[l+k] and s[l]!='?' and s[l+k]!='?'):
                f=False
                break
            if s[l]=='0':
                cnt[0]-=1
            elif s[l]=='1':
                cnt[1]-=1
            else:
                cnt[2]-=1
            l+=1
            dis-=1
        if f:
            print ("YES")
        else:
            print ("NO")
if __name__ == "__main__":
    main()