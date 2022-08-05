# Weier Guo Python
# 08/03/2022

### Introduction ###
# Input: Number Old.Name Bulk Seq.Name Comments
# Print out the list of Seq.Name that need to be combined (bulk 1 or 2).
# Used for running in shell script. 


import os, sys, math
from optparse import OptionParser

usage = ""
parser = OptionParser(usage=usage)
parser.add_option("-f", "--input_file", dest="f", help="Input bulk samples file.")
parser.add_option("-b", "--bulk", dest="b", type="int", help="Choose the bulk (1 or 2).")

(opt, args) = parser.parse_args()


f = open(opt.f,"r")
b = opt.b
o = list()

head = f.readline()
for line in f:
	line = line.split("\n")[0]
	ln = line.split("\t")
	if int(ln[2]) == b:
		o.append(ln[3])

text = " ".join(o)

print(text)


