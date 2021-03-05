#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2021/3/5 11:11
# @url: https://codeforc.es/contest/1256/problem/D
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
## oeis(CROSSREFS):example 1, 3, _, 1260, _, _, _, _, _, 12164510040883200
## sqrt:Decimal(x).sqrt()避免精度误差
## 无穷大表示:float('inf')
## py 10**6 排序+双指针 3秒可能TLE
## 按区间右端点排序,current.left>pre.right,贪心求不相交区间的最大个数
## 加法>位运算
def main():
	q = int(input())
	for i in range(q):
		n, k = map(int, input().split())
		s = str(input())
		pos = []
		for j in range(n):
			if s[j] == '0':
				pos.append(j)
		# print(pos)
		for j in range(len(pos)):
			if pos[j] - j >= k:
				pos[j] = pos[j] - k
				break
			k = k - (pos[j] - j)
			pos[j] = 0
		# print(pos)
		ans = []
		index = -1
		for j in range(len(pos)):
			if pos[j] > 0:
				index = j
				break
		## all 0 move to the head
		if index == -1:
			j = 0
			while j < n:
				if j < len(pos):
					ans.append('0')
				else:
					ans.append('1')
				j += 1
			print("".join(ans))
			continue
		k = 0
		while k < index:
			ans.append('0')
			k += 1
		while index < len(pos):
			while k < pos[index]:
				ans.append('1')
				k += 1
			ans.append('0')
			k += 1
			index += 1
		while k < n:
			ans.append('1')
			k += 1
		print("".join(ans))


if __name__ == "__main__":
	main()
