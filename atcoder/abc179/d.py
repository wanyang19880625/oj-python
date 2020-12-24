# @oj: atcoder
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-09-23 14:24
# @url:https://atcoder.jp/contests/abc179/tasks/abc179_d
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
    # dp
    n,k=map(int,input().split())
    s=[]
    for i in range(k):
        l,r=map(int,input().split())
        s.append((l,r))
    s.sort()
    dp=[0]*(n+1)
    for q in s:
        l,r=q[0],q[1]
        for i in range(l,r+1):
            if i+1<=n:
                dp[i+1]=1
    print (dp)
    mod=998244353
    for i in range(2,n+1):
        for q in s:
            l,r=q[0],q[1]
            dp[i]=dp[i]%mod+dp[i-1]%mod
            if i>=l and i<=r:
                dp[i]=dp[i]%mod+dp[i-l]%mod
            if i>r:
                dp[i]+=dp[i-1]%mod-dp[i-r-1]%mod
    print (dp)                
    print (dp[n]%mod)
if __name__ == "__main__":
    main()