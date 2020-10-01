# Knot65
>For this challenge,a zip file and a paragraph was given.
>When you grep the paragraph for "password", it gives you the hint "it is in three parts,join all the three parts and you'll get the password to the zip"
>Now it is clear that the password of the zip file is broken into three parts and then hidden in this long paragraph.
<br><br>

>After little observation,you'll see that there are very few uppercase chars than the lowercase chars.So,we will write a script for finding all the uppercase chars and concat them in the same order.<br>
[Upper Case Script](https://github.com/echobash/darkCTFWriteups/blob/main/knot65/password.py)
```python
f = open("chall.txt","r")
f = f.read()
password=""
for char in f:
	if char.isupper():
		password+=char
print(password) #IKNOWYARECOLLECTAINGLLUPPERCASELETTERFIRSTPARTOFTHEPASSWORDISLETTHEREBE
print("The first part of password is",password[-10:]) #LETTHEREBE
```

##### So,we have the first part of the password here. LETTHEREBE

> Then for second part of password, it is hidden as whitespaces.
> Running the stegsnow will easily throw the second part of the flag.
```sh
stegsnow -C chall.txt
goodrainswithshining

```

##### So,we have the second part of the password here.  goodrainswithshining

> For the third and last part of the password,there are some homoglyphs unicode characters.
> If you analyze the "ord" of all the characters,there are some outlier values in range of 65000 which are these homoglyph unicode characters only.
> So we can get the third part by running script for all the characters whose decimal value is greater than 65000.

[Homoglyph Script](https://github.com/echobash/darkCTFWriteups/blob/main/knot65/homoglyph.py)
```python
f = open("chall.txt","r")
f = f.read()
thirdPart=""
for char in f:
        if ord(char)>65310:
                thirdPart+=char
print("Third part of the password "+thirdPart)
```
##### The third part of the password we find by this way. #ｒａｉｎｎｎｂｏｗ


### So the password in lowercase:- lettherebegoodrainswithshiningrainnnbow

>Now we have the password for the zip file.
>Once we unzip it with the obtained password,we get a text file [flag.txt](https://github.com/echobash/darkCTFWriteups/blob/main/knot65/flag.txt).
Flag.txt contains some 8-digit numbers separated by space.

>This will be decoded by octal-xlate.
>You can decode it online from [here](https://www.paulschou.com/tools/xlate/)
or write an [script](https://github.com/echobash/darkCTFWriteups/blob/main/knot65/octalXlate.py) to decode octal-xlate.

```python
from Crypto.Util.number import *
ct=[0o31060562, 0o32641524, 0o21475550, 0o14066460, 0o21666171, 0o34073461, 0o35044157, 0o33661564, 0o15046170, 0o23032164, 0o14676400]
flag=""
for c in ct:
       flag+=long_to_bytes(c).decode("utf-8") 
print(flag)
#darkCTF{h0m0Glypw1tHooct4LxL4t3}
```
