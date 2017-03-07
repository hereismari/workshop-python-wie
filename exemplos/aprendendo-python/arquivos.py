#!/usr/bin/python

f = open("file.txt","a+") 
f.write ("something \n")
f.close()

f = open("file.txt","a+") 
print f.read() 



