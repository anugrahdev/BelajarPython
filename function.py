def tokoemas():
    print('Selamat datang')

def hargaemas():

    print('Harga 1 Gram Emas adalah Rp. 2.000.000,')

#membuat function dengan input argumen

def totalharga(g):
    tokoemas()
    hargaemas()
    total = g*2000000
    print('Harga Emas ',g, 'G, adalah Rp.',total)
    print(100 * "=")

totalharga(0.25)
totalharga(0.5)
totalharga(2)
totalharga(15)
