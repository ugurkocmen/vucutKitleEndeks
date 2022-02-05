kilo = float(input("Kilonuzu Giriniz : "))
boy = float(input("Boyunuzu Giriniz : "))

vucutkitleEndeks = kilo / (boy*boy)

try:
    if vucutkitleEndeks < 18:
        print(f"Vücut Kitle Endeksiniz : {vucutkitleEndeks}, Zayıfsınız! ")
    elif vucutkitleEndeks >= 18 and vucutkitleEndeks <25:
        print(f"Vücut Kitle Endeksiniz : {vucutkitleEndeks}, Normalsiniz! ")
    elif vucutkitleEndeks >= 25 and vucutkitleEndeks <30:
        print(f"Vücut Kitle Endeksiniz : {vucutkitleEndeks}, Kilolusunuz! ")
    elif vucutkitleEndeks >= 30 and vucutkitleEndeks <35:
        print(f"Vücut Kitle Endeksiniz : {vucutkitleEndeks}, Obezsiniz! ")
    else:
        print(f"Vücut Kitle Endeksiniz : {vucutkitleEndeks}, Ciddi Obezsiniz!")

except ZeroDivisionError:
    print("Düzgün Yaz Amına Korum Orosbu Çocuğu!")
