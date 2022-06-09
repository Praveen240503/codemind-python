x = int(input())
n = list(map(int,input().split()))
su,nm=0,0
for i in range(0,len(n),2):
    su+=n[i]
for j in range(1,len(n),2):
    nm+=n[j]
nv = su-nm
if nv%4==0:
    print('X')
else:
    print('Y')