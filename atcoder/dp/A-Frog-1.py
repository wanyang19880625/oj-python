n=input()
h=list(map(int,input().split()))
dp=[0]*len(h)
dp[1]=abs(h[1]-h[0])
for i in range(2,len(h)):
    dp[i]=min(abs(h[i-2]-h[i])+dp[i-2],abs(h[i-1]-h[i])+dp[i-1])
print (dp[-1])