# @oj: atcoder
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-05-17 20:54
# @url:
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
    from fractions import Fraction
    n=int(input())
    num=[]
    for i in range(n):
        ab=list(map(int,input().split()))
        f=Fraction(ab[0],ab[1])
        num.append(f)
    print (num)
    d=dict(collections.Counter(num))
    s=set(num)
    k=10**9+7
    def check(n,k):
        ans,m=1,2
        while n>0:
            if n%2==1:
                ans=ans*m%k
            n=n//2
            m=m*m%k
        return ans
    res=check(n,k)-1
    # print (res)
    for x in num:
        if Fraction(-1/x) not in s:
            print (-1/x)
            s.add(x)
        else:
            res=res-check(n-2,k)
    print (res%k)
if __name__ == "__main__":
    main()