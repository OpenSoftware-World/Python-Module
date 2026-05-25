#!/usr/bin/python3
""" Copyright© 2023-2026 OpenSoftware-World
Python-Module Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Python-Module All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/Pyt h on-Module
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/Python-Module """ 

command = str(input('calc> '))
comtxt = "calc> "
about = "Python Hesap Makinesi CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"
sayi1 = float(input(f'{comtxt} 1. sayiyi giriniz: '))
sayi2 = float(input(f'{comtxt} 2. sayiyi giriniz: '))
islem = str(input(f'{comtxt} Gerçekleştirmek İstediğiniz İşlemi Giriniz: '))
top = sayi1 + sayi2 
cık = sayi1 - sayi2 
carp = sayi1 * sayi2 
bol = sayi1 / sayi2 
yuzde = (sayi1 / sayi2) * 100