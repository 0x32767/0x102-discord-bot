# This make file creates a shared object that can be acces from
# ctypes. This file should be run in wsl to access gcc, or g++.
#
# To make the shared object the makefile should be run in this
# way:
# "make file=some_file.c lbname=some_file.so"
#
# NOTE:
# the arguments need to have their file extentions.

CC:=g++

all:
	$(CC) -c -fPIC $(file) -o $(file).o
	$(CC) -shared -Wl,-soname,$(lbname) -o $(lbname)  $(file).o
