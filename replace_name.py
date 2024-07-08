string="i am raushan kumar and i am an engineer"
print(string.replace(" ","_"))
print(string.replace("am","was"))
print(string.find("am",3))
st1=string.find("am")
print(st1)
st2=string.find("am",st1+1)
print(st2)  
name=input("enter your name:")
s1=len(name)
s2=s1+8
print(name.center(s2,"*"))