#!/usr/bin/python

f = open("file.txt","r+") 
f.write ("something \n")
print f.read() 

f.close()


