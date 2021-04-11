#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2021/4/10 22:36
# @url:https://codeforc.es/contest/1512/problem/C
import sys, os
from io import BytesIO, IOBase
import collections, itertools, bisect, heapq, math, string
from decimal import *
from collections import deque

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
## 注意嵌套括号!!!!!!
## 先有思路,再写代码,别着急!!!
## 先有朴素解法,不要有思维定式,试着换思路解决
## 精度 print("%.10f" % ans)
## sqrt:int(math.sqrt(n))+1
## 字符串拼接不要用+操作，会超时
## 二进制转换:bin(1)[2:].rjust(32,'0')
## array copy:cur=array[::]
## oeis(CROSSREFS):example 1, 3, _, 1260, _, _, _, _, _, 12164510040883200
## sqrt:Decimal(x).sqrt()避免精度误差
## 无穷大表示:float('inf')
## py 10**6 排序+双指针 3秒可能TLE
## 按区间右端点排序,current.left>pre.right,贪心求不相交区间的最大个数
## 加法>位运算
def main():
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        s = str(input())
        f = True
        res = list(s)
        l, r = 0, len(s) - 1
        while l <= r:
            if l == r:
                if res[l] == '0':
                    a -= 1
                if res[l] == '1':
                    b -= 1
                break
            if (res[l] == '0' and res[r] == '1') or (res[l] == '1' and res[r] == '0'):
                f = False
                break
            if res[l] == res[r] and res[l] == '0':
                a -= 2
            if res[l] == res[r] and res[l] == '1':
                b -= 2
            if res[l] == '?' and res[r] != '?':
                if res[r] == '0':
                    a -= 2
                    res[l] = '0'
                else:
                    b -= 2
                    res[l] = '1'
            if res[l] != '?' and res[r] == '?':
                if res[l] == '0':
                    a -= 2
                    res[r] = '0'
                else:
                    b -= 2
                    res[r] = '1'
            l += 1
            r -= 1
        # print("".join(res))
        if not f or a < 0 or b < 0:
            print(-1)
            continue
        if a % 2 == 1 and b % 2 == 1:
            print(-1)
            continue
        l, r = 0, len(s) - 1
        while l < r:
            if res[l] == '?' and res[r] == '?':
                if a > 1:
                    a -= 2
                    res[l], res[r] = '0', '0'
                else:
                    if b > 1:
                        b -= 2
                        res[l], res[r] = '1', '1'
            l += 1
            r -= 1
        # print(a, b)
        if a > 0:
            res[len(s) // 2] = '0'
        if b > 0:
            res[len(s) // 2] = '1'
        print("".join(res))


if __name__ == "__main__":
    main()
