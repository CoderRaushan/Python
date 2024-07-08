n=int(input("enter n:"))
if(n%2!=0):
   print("weird")
if(n%2==0):
   if(n>20):
     print("Not Weird")
   elif n in range(2,6):
      print("not weird")
   else:
      print("weird")