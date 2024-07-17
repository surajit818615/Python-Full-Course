str1 ="We wish you a Merry Chirstmas"
print(str1.isprintable()) #returns true if all the variables in the given string are printable

str2 ="        " #using spacebar
print(str2.isspace()) #returns true becouse there is only whitespace
str3 ="       1      "#using tab
print(str3.isspace())#returns false becouse 1 variable is there

str4 ="World Health Organization"
print(str4.istitle())# returns true if the first letter of each word is upper case

str5 ="A lovely girl"
print(str5.istitle()) #returns false if the first letter of each letter is not upper case
 
str6 ="WORLD HEALTH ORGATION"
print(str6.isupper()) #returns true if all the characters are upper case

str7 ="Python is a Interpreted Language"
print(str7.startswith("Python")) #returns true if the string starts with the given value in startswith()

str8 ="I am Surajit Mandal, 21 Years old."
print(str8.swapcase()) #returns uppercase to lowercase and lowercase to uppercase

str9 ="Get a job in NASA is greeat"
print(str9.title()) #capitalise each first letter of the word in the string.
