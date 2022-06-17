#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2022/6/14 22:19
# @url:https://codeforc.es/contest/1692/problem/E
import sys, os
from io import BytesIO, IOBase
import collections, itertools, bisect, heapq, math, string
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
## 注意嵌套括号!!!!!!
## 先有思路,再写代码,别着急!!!
## 先有朴素解法,不要有思维定式,试着换思路解决
## 精度 print("%.10f" % ans)
## sqrt:int(math.sqrt(n))+1
## 字符串拼接不要用+操作，会超时
## 二进制转换:bin(1)[2:].rjust(32,'0')
## array copy:cur=array[::]
## oeis:example 1, 3, _, 1260, _, _, _, _, _, 12164510040883200
## sqrt:Decimal(x).sqrt()避免精度误差
def main():
	t = int(input())
	for i in range(t):
		n, s = map(int, input().split())
		a = list(map(int, input().split()))
		if s > sum(a):
			print(-1)
		else:
			diff = sum(a) - s
			prefix = list(itertools.accumulate(a))
			suffix = list(itertools.accumulate(a[::-1]))
			if diff == 0:
				print(0)
			else:
				# left
				ans = n + 1
				dp1, dp2 = [n + 1] * (diff + 1), [n + 1] * (diff + 1)
				dp1[0] = 0
				dp2[0] = 0
				for j in range(n):
					if prefix[j] > diff:
						break
					dp1[prefix[j]] = min(dp1[prefix[j]], j + 1)
				for j in range(n):
					if suffix[j] > diff:
						break
					dp2[suffix[j]] = min(dp2[suffix[j]], j + 1)
				# print(dp1, dp2)
				for j in range(diff + 1):
					ans = min(ans, dp1[j] + dp2[diff - j], dp1[diff - j] + dp2[j])
				print(ans)


if __name__ == "__main__":
	main()
