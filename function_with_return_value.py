def kuadrat(x):
    total=x**2
    print(x, "kuadrat"" = ",total)

kuadrat(3)

print(100*'=')

def tambah(x,y):
    total=x+y
    print(x, "+", y, "=",total)
    return total

def kali(x,y):
    total = x * y
    print(x, "x", y, "=", total)
    return total

def bagi(x,y):
    total = x / y
    print(x, "/", y, "=", total)
    return total

a=tambah(5,5)
b=kali(5,a)
c=bagi(b,5)