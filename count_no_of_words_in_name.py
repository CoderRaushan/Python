name=input("enter your name:")
n=len(name)
i=0
temp=""
for i in range(0,n):
    if name[i] not in temp:
        temp+=name[i]
        print(f"No of repeatation of {name[i]} is:{name.count(name[i])}")
    i+=1
