# @oj: atcoder
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-11-08 21:18
# @url:https://atcoder.jp/contests/abc182/tasks/abc182_d
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
## 精度 print("%.10f" % ans)
## sqrt:int(math.sqrt(n))+1
## 字符串拼接不要用+操作，会超时
## 二进制转换:bin(1)[2:].rjust(32,'0')
## array copy:cur=array[::]
## oeis:example 1, 3, _, 1260, _, _, _, _, _, 12164510040883200
def main():
    n=int(input())
    a=list(map(int,input().split()))
    prefix=[0]
    # 前缀和
    for i in range(n):
        prefix.append(prefix[-1]+a[i])
    # print ("prefix:",prefix)

    # 前缀和最大值
    mx=[-10**9]
    for i in range(1,n+1):
        mx.append(max(prefix[i],mx[-1]))
    # print ("mx:",mx)

    # 预处理计算每个坐标
    pos=[0]
    for i in range(1,n+1):
        pos.append(prefix[i]+pos[-1])
    # print ("pos:",pos)

    # 根据坐标和前缀和最大值，求每个区间的最大值
    ans=pos[-1]
    for i in range(1,n+1):
        if mx[i]<0:
            ans=max(ans,pos[i-1])
        else:
            ans=max(ans,pos[i-1]+mx[i])
    print (ans)
if __name__ == "__main__":
    main()