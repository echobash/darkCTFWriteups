from Crypto.Util.number import *
ct=[0o31060562, 0o32641524, 0o21475550, 0o14066460, 0o21666171, 0o34073461, 0o35044157, 0o33661564, 0o15046170, 0o23032164, 0o14676400]
flag=""
for c in ct:
       flag+=long_to_bytes(c).decode("utf-8") 
print(flag)
