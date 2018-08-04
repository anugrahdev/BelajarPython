nama="anang"

if nama is "anang":
    print("silahkan masuk")
if nama is not "anang":
    print("anda dilarang masuk")

print(100*"=")

nilai = 75
if 85<=nilai<=100:
    print("anda mendapat nilai A")
elif 75<=nilai<=84:
    print("anda mendapat nilai B")
elif 50<=nilai<=74:
    print("anda mendapat nilai C")
elif 40<=nilai<=49:
    print("anda mendapat nilai D")
else:
    print("anda tidak lulus MK ini")

print(100*"=")
print("operator logikan untuk list dan string")
makanan = ["tekwan","pempek","model","nasi","rendang","sate"]
beli = "nasgor"

if beli in makanan:
    print('Yaa, saya jual makanan ',beli)
if not beli in makanan:
    print('Saya tidak jual makanan ',beli)

print(100*"=")

karakter = "z"

if karakter in beli:
    print('ya ada karakter',karakter,'di dalam sana')
else:
    print('tidak ada karakter', karakter, 'di dalam sana')