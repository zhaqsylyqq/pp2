# --------------------------------------------1
a = [0, 2, 4, 4, 16]
x = "*".join(str(i) for i in a)
print(eval(x))

# --------------------------------------------2
txt = input()
cntup = 0
cntlow = 0
for i in txt:
    if i.isupper():
        cntup += 1
    elif i.islower():
        cntlow += 1
print("Uppercase letters: ", cntup)
print("Lowercase letters: ", cntlow)

# --------------------------------------------3
txt = input()
if txt == txt[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")

# --------------------------------------------4
import time

num = int(input())
milsec = int(input())
sec = milsec / 1000
time.sleep(sec)
sqrt = num**0.5
txt = "Square root of {fnum} after {fsec} is {fsqrt}".format(
    fnum=num, fsec=milsec, fsqrt=sqrt
)
print(txt)

# --------------------------------------------5
mytup = (True, True, False)
mytup2 = (True, True, True)
print(all(mytup))
print(all(mytup2))
