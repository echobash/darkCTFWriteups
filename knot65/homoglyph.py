f = open("chall.txt","r")
f = f.read()
thirdPart=""
for char in f:
        if ord(char)>65310:
                thirdPart+=char
print("Third part of the password "+thirdPart)
