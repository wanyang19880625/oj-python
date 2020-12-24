# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-05-22 13:49
# @url:https://codeforc.es/problemset/problem/1095/C
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
    nk=list(map(int,input().split()))
    n,k=nk[0],nk[1]
    b=[]
    s=n
    if n<k:
        print ("NO")
        return
    if n%2==1:
        n=n-1
        k=k-1
        b=[1]
    if n//2<=k:
        x=k-n//2
        temp=[2]*(n//2-x)+[1]*(2*x)
        b.extend(temp)
        print ("YES")
        print (" ".join([str(x) for x in b]))
        return
    ans=[2]*k
    p=1
    while n!=0:
        n=n//2
        if n<k:
            break
        for i in range(min(n-k,k)):
            ans[i]=ans[i]+2**p
        p=p+1
    b.extend(ans)
    if sum(b)!=s:
        print ("NO")
        return
    print ("YES")
    print (" ".join([str(x) for x in b]))

if __name__ == "__main__":
    main()