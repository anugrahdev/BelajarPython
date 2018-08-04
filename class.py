# Class
class mahasiswa:
    nama='nama'

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim  = input_nim

    def belajar(self,kondisi):
        print(self.nama,'saya belajar',kondisi)

    def tidur(self):
        print(self.nama,'Sedang tidur dikelas')


# Main Program
anang = mahasiswa("Anang Nugraha", 9021381722106)

print(anang.nama)
print(anang.nim)
