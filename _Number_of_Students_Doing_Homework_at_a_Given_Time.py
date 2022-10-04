class Solution:
    def busyStudent(self,startTime,endTime,queryTime):
        ans=0
        m=zip(startTime,endTime)
        for s,e in m:
            if s<=queryTime<=e:
                ans+=1
        return ans
ob=Solution()
c1=int(input())
startTime=list(map(int,input().split()))
c2=int(input())
endTime=list(map(int,input().split()))
queryTime=int(input())

k=ob.busyStudent(startTime,endTime,queryTime)
print(k)