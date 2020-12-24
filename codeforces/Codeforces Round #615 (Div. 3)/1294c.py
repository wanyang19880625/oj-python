# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-05-16 18:09
# @url:https://codeforc.es/contest/1294/problem/C
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
    t=int(input())
    for i in range(t):
        n=int(input())
        s=set()
        f=False
        for a in range(2,math.ceil(math.sqrt(n))+1):
            if n%a==0:
                temp=n//a
                for b in range(a+1,math.ceil(math.sqrt(temp))+1):
                    if temp%b==0 and b!=a and b*b!=temp:
                        s.add(a)
                        s.add(b)
                        s.add(temp//b)
                        f=True
                        break
            if f:
                break
        if f:
            print ("YES")
            print (" ".join([str(x) for x in s]))
        else:
            print ("NO")
if __name__ == "__main__":
    main()