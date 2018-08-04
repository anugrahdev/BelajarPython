Barang = ['laptop','mouse','cangkir','mangkok','piring']

#method

#method menambah di akhir
Barang.append('sendok')
print(Barang)

#menyisipkan
Barang.insert(3,'keyboard')
Barang.insert(3,'laptop')
print(Barang)

Jumlahlaptop = Barang.count('laptop')
print('jumlah laptop dalam list',Jumlahlaptop)

Barang.remove('cangkir')
print(Barang)

Barang.reverse()
print(Barang)

print(100*"=")

stuff=Barang.copy()
stuff.append('kipas')
print(stuff)
print(Barang)