@echo off
where cl >nul 2>nul || "%VS140COMNTOOLS%..\..\VC\vcvarsall.bat" amd64
set INCLUDE=C:\Program Files (x86)\Windows Kits\10\Include\10.0.10240.0\ucrt
set LIB=C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\um\x64;C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\x64
python setup.py build_ext --inplace
