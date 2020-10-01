f = open("chall.txt","r")
f = f.read()
password=""
for char in f:
	if char.isupper():
		password+=char
print(password) #IKNOWYARECOLLECTAINGLLUPPERCASELETTERFIRSTPARTOFTHEPASSWORDISLETTHEREBE
print("The first part of password is",password[-10:]) #LETTHEREBE

thirdPart=""
for char in f:
        if ord(char)>65310:
                thirdPart+=char
print("Third part of the password "+thirdPart)
