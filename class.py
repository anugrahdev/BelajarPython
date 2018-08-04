# Class
class mahasiswa:

    __nilai = 0 # private variable
    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim  = input_nim
        mahasiswa.jumlah_mahasiswa += 1

    def UTS(self,input_nilai):
        self.__nilai += input_nilai

    def UAS(self,input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,'tidak lulus')
        else:
            print(self.nama,'lulus')

# Main Program
anang = mahasiswa("Anang Nugraha", 9021381722106)
kipli = mahasiswa("Kipli Hapijin", 9021381722100)
pajar = mahasiswa("Pajar Hapijin", 9021381722103)


anang.UTS(30)
anang.UAS(55)

anang.check_status()

kipli.UAS(40)
kipli.UTS(10)

kipli.check_status()

print(mahasiswa.jumlah_mahasiswa)
