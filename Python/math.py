import os
#解二次方程
import math

def quadratic(a,b,c):
  d=float(b**2-4*a*c)
  if d<0:
    x0='无解'
    return x0  
  else:
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)  
    return x1,x2

def linearl(b,c):
  x=-1*c/b
  return x    

print('解二次方程\n标准方程：ax+by+c=0') #这是一条注释
a=float(input('输入a：'))
b=float(input('输入b：'))
c=float(input('输入c：'))
if a==0:
    if b==0:
      print('无解')
    else:
      f=linearl(b,c)
      print('X=',f)  
else:  
  s=quadratic(a,b,c)
  if s=='无解':
      print(s)
  else:
    if s[0]==s[1]:
        print('X1=X2=',s[0])
    else:      
        print('X1=',s[0])
        print('X2=',s[1])
os.system('pause')       