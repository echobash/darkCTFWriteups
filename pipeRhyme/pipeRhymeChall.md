## Chall:- Pipe Rhyme
![Pipe Rhyme](https://raw.githubusercontent.com/echobash/darkCTFWriteups/main/pipeRhyme/pipeRhyme.png?token=AEEH7C4LBLMI2ORT2PLVEGK7OYTNI)

Chall Desc:- Wow you are so special.<br>
N=0x3b7c97ceb5f01f8d2095578d561cad0f22bf0e9c94eb35a9c41028247a201a6db95f<br>
e=0x10001<br>
ct=0x1B5358AD42B79E0471A9A8C84F5F8B947BA9CB996FA37B044F81E400F883A309B88<br>

## [Solution](https://github.com/echobash/darkCTFWriteups/blob/main/pipeRhyme/solution.py)


```python
from Crypto.Util.number import *
#You can get factors of it from factor db easily
n=1763350599372172240188600248087473321738860115540927328389207609428163138985769311
p=56129192858827520816193436882886842322337671
q=31415926535897932384626433832795028841
e=65537
ct=810005773870709891389047844710609951449521418582816465831855191640857602960242822
phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(ct,d,n)
m = long_to_bytes(m).decode("utf-8")
print(m)

```

```sh
flag:- darkCTF{4v0iD_us1ngg_p1_pr1mes}

```
