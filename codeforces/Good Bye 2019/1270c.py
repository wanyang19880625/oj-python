# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-05-22 10:17
# @url:https://codeforc.es/problemset/problem/1270/C
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
    ## 异或性质,
    ## 1.任何数异或0都等于本身 例如10^0=10
    ## 2.奇数异或1相当于本身-1 例如5^1=4;偶数异或1相当于+1 例如4^1=5
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        x,s=a[0],a[0]
        for i in range(1,n):
            s=s+a[i]
            x=x^a[i]
        print (2)
        print (x,s+x)
if __name__ == "__main__":
    main()