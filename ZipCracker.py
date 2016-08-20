#!/usr/bin/python
# -*- coding: utf-8 -*-
# Developed By Lil'Essam
import optparse
import zipfile
import atexit
from threading import Thread

def extract_it(zipfile, password):
    try:
        zipfile.extractall(pwd=password)
        print "[+] Password is: " + password + "\n" + "File is extracted successfully"
    except:
        pass
def main():
    parser = optparse.OptionParser("usage %prog "+\
			"-z <zipfile> -d <dicctionary>")
    parser.add_option('-z', dest='zname', type='string',\
				help='Specify the archive file')
    parser.add_option('-d', dest='dname', type='string',\
				help='Specify passwords file')
    (options, arg) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
    	print parser.usage
    	exit(0)
    else:
    	zname = options.zname
    	dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    
    for line in passFile.readlines():
    	password = line.strip('\n')
    	t = Thread(target=extract_it, args=(zFile, password))
    	t.start()
    
def exit_handler():
    print "That's all I could do :(";

atexit.register(exit_handler)
if __name__ == '__main__':
	main()

