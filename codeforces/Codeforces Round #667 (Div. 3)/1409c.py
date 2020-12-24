# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-09-04 22:22
# @url:https://codeforc.es/contest/1409/problem/C
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
    t=int(input())
    for i in range(t):
        n,x,y=map(int,input().split())
        if n==2:
            print (x,y)
            continue
        ans=[]
        if (y-x)%(n-1)==0:
            temp=(y-x)//(n-1)
            ans=[x+i*temp for i in range(n)]
            print (" ".join([str(a) for a in ans]))
            continue
        m=y-x
        for q in range(1,y-x+1):
            if (y-x)%q==0 and (y-x)//q<=n-2:
                m=q
                break
        z=0
        temp=x
        while True:
            temp=temp-m
            if temp<=0 or z>n-2-(y-x)//m:
                break
            ans.append(temp)
            z+=1
        k=0
        while n>z:
            ans.append(x+k*m)
            n=n-1
            k+=1
        print (" ".join([str(a) for a in ans]))

if __name__ == "__main__":
    main()