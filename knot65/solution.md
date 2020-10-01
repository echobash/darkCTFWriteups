For this challenge,a zip file and a paragraph was given.
When you grep the paragraph for "password", it gives you the hint "it is in three parts,join all the three parts and you'll get the password to the zip"
Now it is clear that the password of the zip file is broken into three parts and then hidden in this long paragraph.

After little observation,you'll see that there are very few uppercase chars than the lowercase chars.
Write a script for finding all the uppercase chars and concat them in the same order.

So,we have the first part of the password here. #LETTHEREBE

Then for second part of password, it is hidden as whitespaces.
Running the stegsnow will easily throw the second part of the flag.
By running stegsnow -C chall.txt  #goodrainswithshining

So,now we have the first and the second part of the password.

For the third and last part of the password,there are some homoglyphs unicode characters.
If you analyze the "ord" of all the characters,there are some outlier values in range of 65000 which are these homoglyph unicode characters only.

So we can get the third part by running script for all the characters whose decimal value is greater than 65000.

The third part of the password we find by this way. #ｒａｉｎｎｎｂｏｗ


So the password in lowercase:- lettherebegoodrainswithshiningrainnnbow


Now we have the password for the zip file.

Once we unzip it with the obtained password,we get a text file flag.txt.
Flag.txt contains some 8-digit numbers separated by space.

This will be decoded by octal-xlate.

You can decode it from here. https://www.paulschou.com/tools/xlate/
or write an script to decode octal-xlate.
