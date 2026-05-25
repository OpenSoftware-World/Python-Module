@echo off
@title=Python-Calcutator Setup
:m
cls
echo Python-Calcutator Setup
echo Which Version Do You Want To Install?
echo 1. Python-Calcutator-TR
echo 2. Python-Calcutator-EN
echo Choose:
set input=nothing
set/p input=Choose:
if %input%==TR goto install
if %input%==EN goto install
goto m
:install
echo Python-Calcutator-%input% Version will be downloaded.
pause
copy INSTALL/%input%/calc C:\Users\%users%\
pause
exit