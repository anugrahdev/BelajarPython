number = 44;

for i in range (0,40,1):
    print(i)
    if i is number:
        print('angka ditemukan',i)
        break
else:
    print('angka tidak ditemukan')

print('ini space diluar for')