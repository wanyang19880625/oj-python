# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-08-19 16:16
# @url:https://codeforc.es/contest/1176/problem/C
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
    n=int(input())
    a=list(map(int,input().split()))
    # 4,8,15,16,23,42
    s=set([4,8,15,16,23,42])
    ans=0
    b,c,d,e,f,g=0,0,0,0,0,0
    for x in a:
        if x not in s:
            ans+=1
            continue
        if x==4:
            b+=1
        elif x==8:
            c+=1
            if c>b:
                c-=1
                ans+=1
        elif x==15:
            d+=1
            if d>c:
                d-=1
                ans+=1
        elif x==16:
            e+=1
            if e>d:
                e-=1
                ans+=1
        elif x==23:
            f+=1
            if f>e:
                f-=1
                ans+=1
        elif x==42:
            g+=1
            if g>f:
                g-=1
                ans+=1
    # print (ans,b,c,d,e,f,g)
    print (ans+b+c+d+e+f+g-6*g)
if __name__ == "__main__":
    main()