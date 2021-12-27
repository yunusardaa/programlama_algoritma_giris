# tek basamak
r=["sıfır","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
x=int(input("tek basamaklı tam sayı giriniz: "))
print("\ngiriniz sayı => ",end='')
if (x<0):
   print("eksi ",end='')
print(r[abs(x)])   

