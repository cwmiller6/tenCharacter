#Author: Cole Miller
#Date: 2 March 2016

f = open("input.txt", 'r+')

f2 = open("output.txt", 'r+')

read = f.read()

read2 = f2.readlines()

text = raw_input("What text would you like to write?\n")

f.write(text)

if len(text) > 10:
	f2.write(text)

