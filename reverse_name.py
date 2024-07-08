# name=input("enter your name:")
# print(name [-1::-1])



# dig=input("enter your dig:")
# print(dig [::-1])


# def reverse(l):
  
#     return  l.reverse()
#     return sum
#  var=list(range(1,11))
# var =[ "w","e","r","e","h"]
# reverse(var)
# print(var)



# def reverse(l):
#  g=l[::-1]
#  return g
# # var=list(range(1,11))
# # var =[ "w","e","r","e","h"]
# var=input("enter anything:")
# print(reverse(var))


# def reverse(l):
#  g=l[::-1]
#  return g
# var=list(range(1,11))
# var =[ "w","e","r","e","h"]
# var=input("enter anything:")
# print(reverse(var))

def reverse(l):
   s=[]
   for i in range(1,len(l)+1) :
      h=l.pop()
      s.append(h)
   return s 
# var=[ "w","e","r","e","h"]
var=list(range(1,11))
print(reverse(var))

 