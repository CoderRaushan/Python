def reverse(l1,l2):
    s=[]
    for i in l1 :
     if i in l2 :
        s.append(i)
    return s 
var1=[1,2,5,8]
var2=[1,2,5,6]
print(reverse(var1,var2))
