# Input Output File

#
# w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibaut file baru
# r = read only / hanya bisa baca
# a = appending mode / menambah data di akhir baris
# r+= write and read mode

# Membuat File Text
file = open("data.txt",'w')

file.write("ini adalah text nya")
file.write("\nini baris ke1")
file.write("\nini baris ke3")
file.write("\nini baris ke4")

file.close()

# appending

file3 = open("data.txt",'a')

file3.write("\nbaris ini appending")

file3.close()

# MEMBACA FILE TEXT

file2 = open("data.txt",'r')

print(file2.read())
# print(file2.readline())

file2.close()

