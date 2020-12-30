# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020/12/31 0:38
# @url: https://codeforc.es/contest/1466/problem/E
import sys, os
from io import BytesIO, IOBase
import collections, itertools, bisect, heapq, math, string
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
## 精度 print("%.10f" % ans)
## sqrt:int(math.sqrt(n))+1
## 字符串拼接不要用+操作，会超时
## 二进制转换:bin(1)[2:].rjust(32,'0')
## array copy:cur=array[::]
## oeis:example 1, 3, _, 1260, _, _, _, _, _, 12164510040883200
## sqrt:Decimal(x).sqrt()避免精度误差
def main():
    t = int(input())
    pre = [2**i for i in range(61)]
    print (pre)
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cnt=[0]*61
        for x in a:
            bit=[int(b) for b in list(bin(x)[2:].rjust(61,'0'))]
            for j in range(61):
                cnt[j]+=bit[j]
        s=sum(a)
        print (s,cnt)
        ans=0
        for x in a:
            bit=[int(b) for b in list(bin(x)[2:].rjust(61,'0'))]
            v=s
            for j in range(61):
                if bit[j]!=0:
                    tmp=cnt[j]-bit[j]
                    if tmp<n-1:
                        v+=2**(61-j-1)*(n-1-tmp)
            print (x,v)
            ans+=x*v
        mod = 10**9+7
        print (ans*max(cnt))
if __name__ == "__main__":
    main()
