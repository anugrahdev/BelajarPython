print("Program pembagian")
while True:
    try:
        penyebut = int(input("Masukkan angka penyebut: "))
        pembilang = int(input("Masukkan angka penyebut: "))
        hasil=penyebut/pembilang
        break
    # except Exception as error:
    #     print(error)

    except ValueError:
        print("Yang anda masukkan bukan angka")
    except ZeroDivisionError:
        print("tidak bisa dibagi dengan nol")
    except ImportError:
        print("modul tidak ada")

print("hasilnya ",hasil)