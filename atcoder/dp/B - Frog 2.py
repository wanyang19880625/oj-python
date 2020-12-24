# @oj:atcoder
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-04-20 10:31
# @url:https://atcoder.jp/contests/dp/tasks/dp_b
import sys
def input():
    return sys.stdin.readline().strip()

def main():
    nk=list(map(int,input().split()))
    h=list(map(int,input().split()))
    n=nk[0]
    k=nk[1]
    dp=[10**9]*n
    dp[0]=0
    dp[1]=abs(h[1]-h[0])

    for i in range(2,n):
        # dp[i]=min(dp[j]+abs(h[i]-h[j]) for j in range(max(0,i-k),i))
        for j in range(max(0,i-k),i):
            dp[i]=min(dp[j]+abs(h[i]-h[j]),dp[i])

    print (dp[-1])

if __name__ == "__main__":
    main()