f = open("chall.txt","r")
f = f.read()
password=""
for char in f:
	if char.isupper():
		password+=char
print(password) #IKNOWYARECOLLECTAINGLLUPPERCASELETTERFIRSTPARTOFTHEPASSWORDISLETTHEREBE
print("The first part of password is",password[-10:]) #LETTHEREBE
