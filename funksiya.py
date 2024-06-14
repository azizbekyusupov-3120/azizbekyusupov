# def tyil(ism, yosh):
#     print(f"{ism.title()} {2024-yosh} yoshda")
#
# tyil('shaxnoza',2006)

def kv_kub(son):
    """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")

kv_kub(-4)


def juftmi(son):
    """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son%2:
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")

juftmi(30)
juftmi(152)

def solishtir(x,y):
    """Ikki sonni solishtiruvchi funksiya"""
    if x>y:
        print(f"{x}>{y}")
    elif x<y:
        print(f"{y}>{x}")
    else:
        print(f"{x}={y}")

solishtir(10,20)
solishtir(-9,12)
solishtir(1223*5,5**4)4


def daraja(x,y=2):
    print(f"{x} ning {y}-darajasi {x**y} ga teng")

daraja(5,2)
daraja(3,3)
daraja(94,4)
daraja(6)


def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)