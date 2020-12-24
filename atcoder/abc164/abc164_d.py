# @oj: atcoder
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-04-27 14:27
# @url:https://atcoder.jp/contests/abc164/tasks/abc164_d
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
# (a*b)%p=(a%p*b%p)%p
# (a+b)%p=(a%p+b%p)%p
def main():
    k=2019
    s=str(input())[::-1]
    mod10=[1]
    for i in range(1,len(s)):
        mod10.append((mod10[i-1]%k*10%k)%k)
    inverse=[]
    for i in range(0,len(s)):
        n=int(s[i])
        if n!=0:
            if len(inverse)>0:
                mod=((n%k*mod10[i])%k+inverse[-1])%k
            else:
                mod=((n%k*mod10[i])%k)%k
            inverse.append(mod)
    res=[x for x in list(collections.Counter(inverse).items()) if x[0]==0 or x[1]>1]
    # print (inverse)
    # print (res)
    ans=0
    for r in res:
        if r[0]==0:
            ans+=(r[1]+1)*r[1]//2
        else:
            ans+=(r[1]-1)*r[1]//2
    print (ans)    
    # 181718171
    # print ((1111111117*10+1)%2019,((1111111117%2019*10%2019)%2019%2019+1%2019)%2019)
    # print (8171%2019,((10**3%2019*10%2019)%2019%2019+8171%2019)%2019)
    # print ((11111111171-965)%2019)
if __name__ == "__main__":
    main()