num = int(input("Select you game level: "))
print("Your Free fire game level is: ",num)
if(num>=10):
    print("Your can play clash squad mode.")
    print("You have unlocked all modes - BR, CS, Custom.")
elif(4<=num<10):
    if(num>7):
        print("You can select to play Battle royal ranked mode.")
    else:
        print("You have not enough level to play BR ranked")
else:
    print("You are a noob. You have just started to play free fire.")