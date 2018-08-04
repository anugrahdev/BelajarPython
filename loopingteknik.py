namaband = ['Noah',
            'Ungu',
            'Vagetoz',
            'Kangen Band',
            'Kadal Band']

kumpulanlagu = ['Menunggumu',
                'Laguku',
                'Kehadiranmu',
                'Aku kau dan dia',
                'Cinta tak direstui']

#Mengunakan "enumerate" untuk penomoran list
for i,band in enumerate(namaband, start=1):
    print(i,band)

print("="*99)

#menggunakan ZIP

for band,lagu in zip(namaband,kumpulanlagu):
    print(band, "Memainkkan lagu berjudul:",lagu)

print("="*99)

#set
playlist= {'tetap semangat','ada apa dengan cinta','melupakanmu','terlalu lama sendiri'}

for lagu in sorted(playlist):
    print(lagu)

#Dictionary
print("="*99)
playlist2 = {'Noah' : 'Walau habis terang',
            'Ungu' : 'Cinta dalam hati',
            'Vagetoz' : ' Pergi',
            }

for i,v in playlist2.items():
    print(i,"lagunya",v)