for num in range(0,21):
    for i in range(2,11):
        if(num==2 or num==3):
            print(num)
        elif (num%i==0):
            continue
        else:
            print(num)

