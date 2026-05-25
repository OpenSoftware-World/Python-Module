#!/usr/bin/python3
""" Copyright© 2023-2026 OpenSoftware-World
Python-Module Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Python-Module All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/Python-Module
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/Python-Module """

about = str("Python Calcutator CLI (Command Line Interface) LICENCE=GPL2")
comtxt = "calc> "
command = str(input(comtxt))
about = "Python Calcutator CLI(Command Line Interface) LICENCE=GPL2"
number1 = float(input(f'{comtxt} Enter The 1st number: '))
number2 = float(input(f'{comtxt} Enter The 2st number: '))
process = str(input(f'{comtxt} Enter the Transaction You Want to Perform: '))
addition = number1 + number2
subraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
Percentage = (number1 / number2) * 100