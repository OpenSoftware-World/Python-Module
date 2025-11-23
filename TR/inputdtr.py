#!/usr/bin/python3
""" Copyright© 2023-2025 OpenSoftware-World
Python-Module Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Python-Module All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/Python-Module
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/Python-Module """

command=input('calc> ')
comtxt="calc> "
about="Python Hesap Makinesi CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"
sayi1=input('{0} 1. sayiyi giriniz: '. format(comtxt))
sayi2=input('{0} 2. sayiyi giriniz: '. format(comtxt))
islem=input('{0} Gerçekleştirmek İstediğiniz İşlemi Giriniz: '. format(comtxt))
top=float(sayi1)+float(sayi2)
cık=float(sayi1)-float(sayi2)
carp=float(sayi1)*float(sayi2)
bol=float(sayi1)/float(sayi2)
yuzde=float(sayi1)%float(sayi2)