# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-05-26 11:16
# @url:https://codeforc.es/problemset/problem/897/B
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
    kp=list(map(int,input().split()))
    k,p=kp[0],kp[1]
    res=[00,11,22,33,44,55,66,77,88,99]
    if k<=9:
        print (sum(res[1:k+1])%p)
    else:
        m=1
        cnt,i,t,r=9,1,0,0
        while True:
            for j in range(10):
                if cnt==k:
                    break
                x=res[i]//(10**m)
                y=res[i]%(10**m)
                x=x*(10**(m+2))
                res.append(res[j]*(10**m)+x+y)
                t=t+1
                r=r+1
                cnt=cnt+1
            # print (res[i],m,t)
            if cnt==k:
                break
            if t==10:
                t=0
                i=i+1
            if r==9*10**m:
                r=0
                m=m+1
        # print (res)
        print (sum(res)%p)
if __name__ == "__main__":
    main()