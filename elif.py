num = float(input("Enter Your SGPA: "))
print("So, in 6th sem your SGPA is ", num)
if(7.50<num<9.9):
    print("You get a best score in the exam. You pass the exam.")
elif(num>9.9):
    print("Error : Enter correct SGPA.")
elif(5.54<num< 7.50):
    print("Your score is lower than average and if gor xp. You have an backlog.")
else:
    print("You fail in the exam.")
