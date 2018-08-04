Data = [1,2,4,8,16,32,64,128,256]

#Mengakses List
Subdata1 = Data[3]
Subdata2 = Data[-3]

#Memotong List
Subdata3 = Data[2:4]
Subdata4 = Data[:4]

Data2 = [0,3,5,7,9,11,13,15,17]

#Menambahlist
Data3 = Data+Data2

#merubah konten list

print(Data)
print("="*100)
#Data[1]=22

#mengcopy data list ke variable baru
a=Data[:]
a[4]=100

#Mengubah content list dengan mnggunakan metode slicing
Data[3:5]=[11,12]

#list dalam list

x=[Data,Data2]

#mengakses list dalam multi dimentional list

y = x[1][3]
print(x)
print(y)

#method untuk list
Data.append(69)
print(100*"=")
print(Data)

print(100*"=")

##FUNCTION UNTUK LIST

panjang=len(Data)
print(panjang)