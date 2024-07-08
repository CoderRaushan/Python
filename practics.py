name,age=input("enter your name and age:").split(" ")
s1=name.lower()
age=int(age)
s2=s1[0]
s3="a"
if s3==s2 and age >=10:
    print("you can watch coco")
else:
    print("you can not watch coco")