str1 = "ABcDEfghIJ" #string
print(str1.upper()) #converts a string to upper case
print(str1.lower()) #converts a string to lower case

str2 = "   Jonny Silverhand   " #string2
print(str2)               #exactly print form of string 2
print(str2.strip())       #removes any white spaces befroe and after the string

str3 ="Hello!!!!!!"       #string3
print(str3.rstrip("!"))   #removes any tralling characters

str4 ="Surajit Mandal"   #string4
print(str4)              #print str4
print(str4.replace("ajit","vi"))     #str4 ajit replaces in vi strings
print(str2.replace("sp","M"))        #replaces sp in M

str5 ="Silver Spoon precious Thing"
print(str5.split(" ")) #split the string at the whitespace

str6 = "hello"
capStr1 = str6.capitalize() #turns only the first character of the string to uppercase
print(capStr1)
str7 = "hello WorlD"
capStr2 = str7.capitalize() #turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase
print(capStr2)

str8 = "Welcome to the Console!!!"
print(str8.center(50))             #The center() method aligns the string to the center as per the parameters given by the user.
str9 = "Welcome to the Console!!!"
print(str9.center(50, "."))

str10 = "Abracadabra"
countStr = str10.count("a") #returns the numberof time given value has occured
print(countStr)

str11 = "Welcome to the Console !!!"
print(str11.endswith("!!!"))

str12 = "He's name is Dan. He is an honest man."
print(str12.find("is")) # the find() method searches for the first occurrence of the given value and returns the index where it is present. 
str13 = "He's name is Dan. He is an honest man."
print(str13.find("Daniel"))#If given value is absent from the string then return -1.

str14 = "He's name is Surajit. Surajit is a bad boy."
print(str14.index("Surajit"))   #it scarches the first occurance of the given value

str15 ="Welcometotheconsole2024"
print(str15.isalnum()) #returns true if the entire string only consist of A-Z,a-z,0-9

str16 ="Surajit Bhai !!! #sm"
print(str16.isalnum()) #returns false

str17 ="Welcome" 
print(str17.isalpha()) #returns true if the entire string only consist of A-z, a-z

str18 = "Welcome2024"
print(str18.isalpha()) #returns false

str19 ="Hello World"
print(str19.islower())#returns true if the entire string only consist of lower case characters










