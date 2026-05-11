#!/usr/bin/python3
from inputd import *

select=input('İşlem Giriniz: ')

if select=="top":
    add()
elif select=="cık":
    sub()
elif select=="carp":
    mul()
elif select=="bol":
    div()
elif select=="yuzde":
    per()
else:
    print("Hiç bir işlem girilmedi...")