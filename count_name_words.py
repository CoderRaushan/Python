name=input("enter your name:")
n=len(name)
i=0
temp=""
while i<n: 
    if name[i] not in temp:
        temp+=name[i]
        print(f"No of repeatation of {name[i]} is:{name.count(name[i])}")
    i+=1
