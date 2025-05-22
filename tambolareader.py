from random import randrange
from os import system
from playsound import playsound
 
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

def plist(l,i,n):
  for x in range(90):
    if l[x]==i and i!=0:
      print("  ~%3d"%(l[x]),end="")
    elif l[x]==n and n!=0:
      print("  *%3d"%(l[x]),end="")
    else:
      print("%6d"%(l[x]),end="")
    if (x+1)%10==0:
      print()

l90=randlist(90,90)
l2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n=0
system("cls")
print("\n\n\t    ~~~~~ Welcome to T-A-M-B-O-L-A Game ~~~~~")
print("\n\n\t           by**Sathvik Narayanasetty**      \n\n")
plist(l2,n,n)
playsound("d:\\sathvik\\python\\audio\\welcome.mp3")
playsound("d:\\sathvik\\python\\audio\\preface.mp3")
input("\n\nPress ENTER to start the GAME ...")
for i in l90:
  system("cls")
  l2[i-1]=i
  fn="d:\\sathvik\\python\\audio\\telugu"+str(i)+".mp3"
  print("\n\n\t    ~~~~~ Welcome to T-A-M-B-O-L-A Game ~~~~~")
  print("\n\n\t           by**Sathvik Narayanasetty**      \n\n")
  plist(l2,i,n)
  print("\n\nReading ~%2d (%s), Prev # *%2d"%(i,fn,n),end="",flush=True)
  playsound(fn)
  n=i
  if i!=l90[89]:
    input("\n\nPress ENTER to continue...")

playsound("d:\\sathvik\\python\\audio\\end.mp3")