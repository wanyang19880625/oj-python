# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-08-20 16:23
# @url:https://codeforc.es/problemset/problem/1105/C
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
def main():
    mod=10**9+7
    n,l,r=map(int,input().split())
    t,m=(r-l+1)//3,(r-l+1)%3
    mod0,mod1,mod2=t,t,t
    if m==1:
        if l%3==0:
            mod0=t+1
        elif l%3==1:
            mod1=t+1
        elif l%3==2:
            mod2=t+1
    elif m==2:
        if l%3==0:
            mod0,mod1=t+1,t+1
        elif l%3==1:
            mod1,mod2=t+1,t+1
        elif l%3==2:
            mod2,mod0=t+1,t+1
    # print (mod0,mod1,mod2)

    dp=[[0]*3 for i in range(n)]
    dp[0][0],dp[0][1],dp[0][2]=mod0,mod1,mod2

    for i in range(1,n):
        dp[i][0]=dp[i-1][0]*mod0%mod+dp[i-1][1]*mod2%mod+dp[i-1][2]*mod1%mod
        dp[i][1]=dp[i-1][0]*mod1%mod+dp[i-1][1]*mod0%mod+dp[i-1][2]*mod2%mod
        dp[i][2]=dp[i-1][0]*mod2%mod+dp[i-1][1]*mod1%mod+dp[i-1][2]*mod0%mod
        # dp[i][0]=dp[i][0]%mod
        # dp[i][1]=dp[i][1]%mod
        # dp[i][1]=dp[i][2]%mod
    print (dp[n-1][0]%mod)
if __name__ == "__main__":
    main()