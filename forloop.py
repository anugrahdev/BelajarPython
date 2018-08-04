#list sebagai iterable
makanan = ['pempek','tekwan','bakso','mie ayam','seblak','dodol']

for g in makanan:
    print(g)
    print(len(g))
print(100*"=")
#String sebagai iterable

seblak="seblak"

for i in seblak:
    print(i)
print(100*"=")
#for di dalam for

buah  = ['jeruk','melok','alpukat','pisang','anggur','semangka']
sayur = ['bayam','kubis','tomat','selada','wortel','kentang']

Daftarbelanja = [makanan,buah,sayur]
print(Daftarbelanja)
print(100*"=")
for subDaftarbelanja in Daftarbelanja:
    print(subDaftarbelanja)
    for komponen in subDaftarbelanja:
        print(komponen)
