#!/usr/bin/python3
""" Copyright© 2023-2026 OpenSoftware-World
Python-Module Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Python-Module All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/Python-Module
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/Python-Module """

from inputdtr import *

if command in ("calc", "Calc", "calculator", "Calculator"):
   print("calc> Girebileceğiniz işlemler: ")
   print("top\ncık\n\carp\nbol\nyuzde\nabout")
   sayi1 , sayi2 , islem
   if islem in ("toplama", "Toplama", "+"): 
     print(f"{sayi1} + {sayi2} = {top}")
   elif islem in ("çıkarma", "Çıkarma", "-"):
     print(f"{sayi1} + {sayi2} = {cık}")
   elif islem in ("çarpma", "Çarpma", "*"):
     print(f"{sayi1} + {sayi2} = {carp}")
   elif islem in ("bölme", "Bölme", "/"):
     if sayi2 == 0:
         print("0'a bölünemez. Lütfen 0'dan farklı bir sayı giriniz.")
     else:
         print(f"{sayi1} + {sayi2} = {bol}")
   elif islem in ("yüzde alma", "Yüzde alma", "%"):
     print(f"{sayi1} + {sayi2} = {yuzde}")
   else:
       print("Geçersiz İşlem")
if command in ("about", "About", "info", "Info", "information", "Information"):
     print(about)
elif command in ("exit", "Exit"):
     exit()
elif command in ("help", "Help", "list", "List", "commands", "commands-list"):
     print("Python calc Help")
     print("\n Command: calc , about , help , exit , git-address , web-site , ver , licence")
elif command in ("git-address", "OpenSoftware-World GitHub Address", "GitHub Link", "GitHub Page"):
     print("Github Link: https://github.com/OpenSoftware-World")
elif command in ("web-site", "Web site", "Web Site"):
     print("https://opensoftware-world.com")
elif command in ("ver", "Ver", "version", "Version"):
     print("Sürüm: 0.1.7 (Son Güncellenme Tarihi 8 Eylül , 2023 , 18:08)")
elif command in ("licence", "Licence", "Licence info"):
     print("This Software is protected under the GPL2 license")
else:
     print("Geçersiz Komut")