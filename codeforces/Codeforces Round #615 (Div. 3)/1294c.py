# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-05-16 18:09
# @url:https://codeforc.es/contest/1294/problem/C
import sys, os
from io import BytesIO, IOBase
import collections, itertools, bisect, heapq, math, string

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
	t = int(input())
	for i in range(t):
		n = int(input())
		v = n
		prime_factor = collections.defaultdict(lambda: 0)
		i = 2
		while i * i <= v:
			while v % i == 0:
				prime_factor[i] += 1
				v = v // i
			i += 1
		if v != 1:
			prime_factor[v] += 1
		# print(prime_factor)
		keys = list(prime_factor.keys())
		if len(keys) == 1:
			k = keys[0]
			if prime_factor[k] < 6:
				print("NO")
			else:
				print("YES")
				print(k, k * k, n // (k ** 3))
		elif len(keys) == 2:
			k1, k2 = keys[0], keys[1]
			if prime_factor[k1] + prime_factor[k2] >= 4:
				print("YES")
				print(k1, k2, n // (k1 * k2))
			else:
				print("NO")
		else:
			k1, k2 = keys[0], keys[1]
			print("YES")
			print(k1, k2, n // (k1 * k2))


if __name__ == "__main__":
	main()
