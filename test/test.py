#!/usr/bin/python3
""" Copyright© 2023-2026 OpenSoftware-World
Python-Module Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Python-Module All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/Python-Module
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/Python-Module """

select = str(input('İşlem Giriniz: '))

sayi1 = int(input('1.sayiyi giriniz: '))
sayi2 = int(input('2.sayiyi giriniz: '))

if select in ("toplama", "Toplama", "+"):
    print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
elif select in ("çıkarma", "Çıkarma", "-"):
    print(f"{sayi1} + {sayi2} = {sayi1 - sayi2}")
elif select in ("çarpma", "Çarpma", "*"):
    print(f"{sayi1} + {sayi2} = {sayi1 * sayi2}")
elif select in ("bölme", "Bölme", "/"):
    if sayi2 == 0:
        print("0'a bölünemez. Lütfen 0'dan farklı bir sayı giriniz.")
    else:
        print(f"{sayi1} + {sayi2} = {sayi1 / sayi2}")
elif select in ("yüzde alma", "Yüzde alma", "%"):
    print(f"{sayi1} + {sayi2} = {(sayi1 / sayi2)*100}")
else:
    print("Hiç bir işlem girilmedi...")