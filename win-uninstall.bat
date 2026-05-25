@echo off
@title=Python-Calcutator Uninstall
:m
cls
echo Python-Calcutator Uninstall
echo Which Version Do You Want To Uninstall?
echo Are you sure you want to uninstall Python-Calculator from your system?
echo Choose:
set input=nothing
set/p input=Choose:
if %input%==Y goto uninstall
if %input%==N exit
goto m
:uninstall
if %input%==1 set input=TR
if %input%==2 set input=EN
echo Python-Calcutator-%input% Uninstall.
pause
del C:\Users\%users%\calc
pause
exit