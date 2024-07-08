# def check(name):
#     s=name[::-1]
#     if s==name:
#         return "true"
#     else :
#         return "false"

# name=input("enter name:")
# print(check(name))

def user_info(firsr_name,last_name,age=34):
    print(f"firsr_name is:{firsr_name}")
    print(f"last_name is:{last_name}")
    print(f"age is:{age}")


firsr_name=input("enter first_name:")
last_name=input("enter last_name:")
age=input("enter age:")
user_info(firsr_name,last_name)



