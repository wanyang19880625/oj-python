# @oj: atcoder
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-06-05 15:25
# @url:https://atcoder.jp/contests/abc169/tasks/abc169_d
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
    #判断n是否为素数
    def isprime(n):
        if n <= 1:
            return 0
        for x in range(2,int(math.sqrt(n))+1):
            if n%x == 0:
                return 0
        return 1
    #利用递归分解n并打印质因数
    ans=[]
    def bprime(n):
        if isprime(n):
            ans.append(n)
        else:
            x = 2
            while x <= int(n/2):
                if n%x == 0:
                    ans.append(x)
                    return bprime(n//x)
                x = x + 1
    bprime(n)
    # print (ans)
    d=collections.Counter(ans)
    mx=0
    for k in d.keys():
        i=1
        v=d[k]
        cnt=0
        while v>0:
            v=v-i
            i=i+1
            cnt+=1
        if v==0:
            mx+=cnt
        else:
            mx+=(cnt-1)
    print (mx)
if __name__ == "__main__":
    main()