# def greater(x,y):
#     if x>=y:
#         return x
#     else:
#         return y
# x=int(input("enter your number x:"))
# y=int(input("enter your number y:"))
# s=greater(x,y)
# print(f"{s} is greater")



# def greater(x,y,z):
#     if x>=y and x<=z:
#         return x
#     elif y>=x and y>=z:
#         return y
#     else:
#         return z
# x=int(input("enter your number x:"))
# y=int(input("enter your number y:"))
# z=int(input("enter your number y:"))
# s=greater(x,y,z)
# print(f"{s} is greater")
def greater(x,y,z):
    if x>=y and x<=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z
x=int(input("enter your number x:"))
y=int(input("enter your number y:"))
z=int(input("enter your number y:"))
s=greater(x,y,z)
print(f"{s} is greater")