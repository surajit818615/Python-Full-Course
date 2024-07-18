#while loop in python
count = 5;
while(count>0):
    print(count)
    count = count -1
#else with while loop
x = int(input("Enter a number: "))
while(0<x<10):
    print(x)
    x=x-1
else:
    print("Counter is 0")

#do while loop in python.
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        print("Your number is negative. Enter correct value.")
        break