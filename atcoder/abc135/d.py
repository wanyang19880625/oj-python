# @oj: atcoder
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-05-19 17:18
# @url:https://atcoder.jp/contests/abc135/tasks/abc135_d
import sys,os
from io import BytesIO, IOBase
import collections,itertools,bisect,heapq,math,string
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
    # python取模注意每次都需要取模，否则可能会导致tle
    # 大数取模的运算通常可以分解为每个位置的权重进行取模运算，然后求和再取模的，例如：
    # 1993%mod=(1000%mod+900%mod+90%mod+3%mod)%mod
    # 利用模运算的基本性质：
    # 加法：19%3=(10%3+9%3)%3 (a+b)%mod=(a%mod+b%mod)%mod
    # 乘法：27%4=(9%4*3%4)%4  (a*b)%mod=(a%mod*b%mod)%mod
    s=str(input())
    S=s[::-1]
    dp=[[0]*13 for i in range(len(S))]
    mod=10**9+7
    p=1 # 每位的权重10的幂次
    for i in range(len(S)):
        if i==0:
            if S[i]!='?':
                t=p*int(S[i])%13
                dp[i][t]+=1
            else:
                for j in range(10):
                    dp[i][j]+=1
        else:
            if S[i]!='?':
                t=p*int(S[i])%13
                for j in range(13):
                    dp[i][(t+j)%13]=dp[i-1][j]%mod
            else:
                for j in range(10):
                    for k in range(13):
                        temp=(p*j%13+k)%13
                        dp[i][temp]=(dp[i][temp]+dp[i-1][k])%mod
        # 权重取模
        p=(p%13*10%13)%13
    # print (dp)
    print (dp[len(S)-1][5])
if __name__ == "__main__":
    main()