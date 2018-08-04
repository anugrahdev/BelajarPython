def siswa(nama):
    print('nama siswa adalah:',nama)

siswa("anang")

def guru (nama,matapelajaran):
    print('nama guru adalah:',nama,"mengajar mata pelajaran:",matapelajaran)

guru(matapelajaran='alpro',nama='dian')

def karyawan(nama,tempat,shift='malam'): #default pada shift
    print('nama karyawan :',nama)
    print('shift: ',shift)
    print('tempat tugas',tempat)

karyawan('anang',tempat='palembang')
