@echo off
title Python-Calculator Setup
:m
cls
echo Python-Calculator Setup
echo Which Version Do You Want To Install?
echo 1. Python-Calculator-TR
echo 2. Python-Calculator-EN
set /p input=Choose:
if "%input%"=="1" set input=TR
if "%input%"=="2" set input=EN
if /I "%input%"=="TR" goto install
if /I "%input%"=="EN" goto install
goto m
:install
echo Python-Calculator-%input% Version will be downloaded.
pause
copy "Install\%input%\calc" "C:\Users\%USERNAME%\"
pause
exit