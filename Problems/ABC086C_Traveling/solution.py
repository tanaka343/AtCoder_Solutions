N=int(input())
t0,x0,y0=0,0,0
flg=True
for i in range(N):
  t,x,y=map(int,input().split())
  if abs(t-t0) >= (abs(x-x0)+abs(y-y0))and abs(t-t0)%2==(abs(x-x0)+abs(y-y0))%2:
    flg=True
    t0,x0,y0=t,x,y
  else:
    flg=False
    break
if flg==True:
  print('Yes')
else:
  print('No')
