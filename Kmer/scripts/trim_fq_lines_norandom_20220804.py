# Weier Guo Python
# 08/04/2022

### Introduction ###
# Trim .fq files to have similar reads depth for the two bulks. 


import os, sys, math
from optparse import OptionParser

usage = ""
parser = OptionParser(usage=usage)
parser.add_option("-f", "--input", dest="f", help="Input fq file.")
parser.add_option("-r", "--remained", dest="r", type="int", help="Input intended remained line.")
parser.add_option("-o", "--output", dest="o", help="Output file.")

(opt, args) = parser.parse_args()

### SET PARAMETERS AND FILES ###
f = open(opt.f,"r")
r = opt.r 
o = open(opt.o,"w")
i = 0 

for line in f:
	if i <= r:
		o.write(line)
		i += 1

f.close()
o.close()
