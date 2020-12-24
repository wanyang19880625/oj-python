# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-05-26 17:25
# @url:https://codeforc.es/contest/1247/problem/D
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
    nk=list(map(int,input().split()))
    n,k=nk[0],nk[1]
    a=list(map(int,input().split()))
    b=sorted(a)
    mx=b[-1]*b[-2]
    # print (math.log(10**10,2))
    p=[]
    for x in range(1,math.ceil(math.sqrt(mx))+1):
        if x**k<=mx:
            p.append(x**k)
    d=collections.defaultdict(list)
    for i,v in enumerate(a):
        d[v].append(i)
    # print (d)
    # print (p)
    ans=0
    key=set(d.keys())
    for x in p:
        s=set()
        for y in key:
            # print (x,y)
            if x%y==0 and y not in s and x//y in d.keys():
                s.add(y)
                s.add(x//y)
                l=d[x//y]
                # print (y,x//y,d[y],d[x//y])
                if y==x//y:
                    ans+=(len(l)-1)*len(l)//2
                else:
                    ans+=(len(l)*len(d[y]))
                    # for index in d[y]:
                    #     j=bisect.bisect_right(l,index)
                    #     print (index,d[x//y],j,len(l)-j)
                    #     if len(l)-j>0:
                    #         ans+=(len(l)-j)                
    print (ans)
if __name__ == "__main__":
    main()