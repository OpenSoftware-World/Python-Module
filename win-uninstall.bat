@echo off
title Python-Calculator Uninstall
:m
cls
echo Python-Calculator Uninstall
echo Which Version Do You Want To Uninstall?
echo Are you sure you want to uninstall Python-Calculator from your system? (Y/N)
set /p input=Choose:
if /I "%input%"=="Y" goto uninstall
if /I "%input%"=="N" exit
goto m
:uninstall
echo Enter the version of Python-Calculator you want to uninstall. (TR/EN)
set /p lang=Choose:
if /I "%lang%"=="TR" set lang=TR
if /I "%lang%"=="EN" set lang=EN
echo Python-Calculator-%lang% Uninstall.
pause
del C:\Users\%USERNAME%\calc
pause
exit