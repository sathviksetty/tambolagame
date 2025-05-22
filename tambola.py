from random import randrange
from math import floor
def randlist(n1,n2):
  l=[]
  c=0
  while True:
    r=randrange(1,n1+1)
    if r not in l:
      l.append(r)
      c=c+1
      if c==n2:
        break
  return l

def randlist5(n1,n2):
  global l90
  l=[]
  c=0
  while True:
    r=randrange(1,n1+1)
    if r not in l:
      for x in l90:
        if floor(x/10)==r-1:
          l.append(r)
          c=c+1
          break
    if c==n2:
      break
  return l

def println(l5):
  global l90
  for j in range(1,10):
    if j in l5:
      y=j*10
      for x in l90:
        if ((y-x >=1 and y-x <=10) or (j==9 and x==90)):
          print ("%3d"%(x),end="")
          f.write(str(x)+",")
          l90.remove(x)
          break
    else:
      print("   ",end="")
      f.write(str(0)+",")
  print()
  f.write("\n")



f=open("tambola.csv","at")
l90=randlist(90,90)

for i in range(15): #print first 15 rows
  l5=randlist5(9,5)
  l5.sort()
  println(l5)
  if (i+1)%3==0:
    print()

l5=[]
for i in range(15): #print last 15 numbers
  l5.append(l90[i])
  if (i+1)%5==0:
    l5.sort()
    for x in l5:
      print ("%3d"%(x),end="")
      f.write(str(x)+",")
    l5=[]
    print() 
    f.write("\n")
f.close()