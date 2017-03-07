#!/usr/bin/python

f = open("file.txt","a+") 
f.write ("something \n")
print f.read() 

f.close()


