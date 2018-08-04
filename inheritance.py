class Ojek():
    def __init__(self,nama,motor,daerah):
        self.nama = nama
        self.motor = motor
        self.daerah = daerah

    def cek_id(self):
        print('nama:',self.nama,'\nmotor:',self.motor,'\ndaerah:',self.daerah,'\n')

class Gojek(Ojek):
    def cek_id(self):
        print('Cek Di Aplikasi Gojek')

ojek1 = Ojek('Anang Nugraha','MX King','Lunjuk')
ojek2 = Ojek('Pajar Diputra','NMAX','KI')
ojek3 = Gojek('Aldi Cringe','R15','KM 5')

ojek1.cek_id()
ojek2.cek_id()
ojek3.cek_id()