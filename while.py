angka=0

while angka<=5:
    print('niainya adalah:',angka)
    angka=angka+1

print('diluar while')

print(100*"=")

start = True

while start:
    print('di dalam while')
    if angka is 100:
        start = False
        print('angka 100 di temukan')
    angka += 1