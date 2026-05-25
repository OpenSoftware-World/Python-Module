#!/usr/bin/python3
""" Copyright© 2023-2026 OpenSoftware-World
Python-Module Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Python-Module All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/Python-Module
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/Python-Module """

from inputden import *

if command=="calc":
    print("calc> Transactions You Can Enter: ")
    print("collect\nExtraction\n\Impact\nDivide\nPercentage\nabout")
    number1 , number2 , process
    if process in ("collect", "Collect", "+"): 
       print(f"{0} + {1} = {2}". format(number1,number2,collect))  
    elif process in ("Extraction", "extraction", "-"):
       print(f"{0} - {1} = {2}". format(number1,number2,Extraction))
    elif process in ("multiplication", "Multiplication", "*"):
       print(f"{0} * {1} = {2}". format(number1,number2,Impact))
    elif process in ("divide", "Divide", "/"):
       print(f"{0} / {1} = {2}". format(number1,number2,Divide))
    elif process in ("percentage", "Percentage", "%"):
       print(f"{0} % {1} = {2}". format(number1,number2,Percentage))
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
   print("Version: 0.1.5.5 (Last Updated September 6 , 2023 , 22:22)")
elif command in ("licence", "Licence", "Licence info"):
   print("This Software is protected under the GPL2 license")