#!/usr/bin/python3
""" Copyright© 2023-2026 OpenSoftware-World
Python-Module Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Python-Module All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/Python-Module
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/Python-Module """

# Calcutator inputs

def calc_input(lang):
    global not_zero_div
    if lang == "en" or lang == "EN" or lang == "English":
        number1_str= "Enter the First Number: "
        number2_str= "Enter the Second Number: "
        not_zero_div = "It cannot be divided by 0."
    elif lang == "tr" or lang == "TR" or lang == "Turkish" or lang == "Türkçe":
        number1_str= "1.sayiyi giriniz: "
        number2_str= "2.sayiyi giriniz: "
        not_zero_div = "0'a bölünemez."
    number1=float(input(number1_str))
    number2=float(input(number2_str))
    return number1, number2

def add(lang):
    number1, number2 = calc_input(lang)
    print(f"{number1} + {number2} = {number1 + number2}")

def sub(lang):
    number1, number2 = calc_input(lang)
    print(f"{number1} - {number2} = {number1 - number2}")

def mul(lang):
    number1, number2 = calc_input(lang)
    print(f"{number1} * {number2} = {number1 * number2}")

def div(lang):
    number1, number2 = calc_input(lang)
    if number2 == 0:
        print(not_zero_div)
        return
    print(f"{number1} / {number2} = {number1 / number2}")

def per(lang):
    number1, number2 = calc_input(lang)
    print(f"{number1} % {number2} = {(number1 / number2) * 100}")

# number,letter inputs (for random)

numbers = [0,1,2,3,4,5,6,7,8,9,10]
letters= "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"