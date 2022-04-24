a,b,c = map(float,input().split())
s=(a+b+c)/2
import math
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("%.2f"%area)