mahasiswa1 = {"NIM":106,
             "Nama":"Anang Nugraha",
             "Prodi":"Teknik Informatika",
             "Status Mahasiswa":"Aktif"}

mahasiswa2 = {"NIM":104,
             "Nama":"Aerosh Nugraha",
             "Prodi":"Sistem Informasi",
             "Status Mahasiswa":"Aktif"}

print(mahasiswa1["Nama"])
print(mahasiswa1.keys())
print(mahasiswa1.values())
print(mahasiswa1.items())

print(100*"=")

list_mahasiswa = {106:mahasiswa1,104:mahasiswa2}
print(list_mahasiswa[104])