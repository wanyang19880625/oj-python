# @oj: atcoder
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-05-10 21:37
# @url:https://atcoder.jp/contests/abc167/tasks/abc167_d

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
    A=list(map(int,input().split()))
    pos=[1]
    cnt=0
    s=set()
    s.add(1)
    while cnt<len(A):
        temp=A[pos[-1]-1]
        pos.append(temp)
        # 注意要使用set来判断集合元素是否存在,
        # 不能使用 in pos的操作，数组的in存在超时的风险
        if temp in s:
            # pos.append(A[pos[-1]-1])
            break
        s.add(temp)
        cnt+=1
    # print (pos)
    index=pos.index(pos[-1])
    # 注意k小于第一次出现重复周期数字的情况
    if k<index:
        print (pos[k])
    else:
        mod=(k-index)%(len(pos[index:])-1)
        # print (mod)
        print (pos[index+mod])
if __name__ == "__main__":
    main()
