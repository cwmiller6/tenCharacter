#Author: Cole Miller
#Date: 2 March 2016

#Open the two files
f = open("input.txt", 'r+')

f2 = open("output.txt", 'r+')

read = f.read()

read2 = f2.read()

text = raw_input("What text would you like to write?\n")

#Write the original input with no limitations to input file 
f.write(text)

#If the text is more than ten characters write the limited to ten characters version on the ouput file
if len(text) > 10:
	f2.write(text[0:10])