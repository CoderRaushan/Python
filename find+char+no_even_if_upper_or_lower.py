name,char=input("enter your name and a character:").split(",")
print(f"no of length of your neme is:{len(name)}")
print(f"no of char is:{name.strip().lower().count(char.strip().lower())}")