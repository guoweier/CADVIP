# Weier Guo Python
# 09/04/2022

# Introduction:
# A script for selecting kmers significantly appeared in two bulks.
# Input format: Kmer Bulk1 Bulk2
# Selecting kmers appear 0 either in Bulk1 or Bulk2. 

import os, sys, math
from optparse import OptionParser

usage = ""
parser = OptionParser(usage=usage)
parser.add_option("-f", "--input", dest="f", help="Input bulk table.")
parser.add_option("-t", "--threshold", dest="t", type="int", default=0, help="Input threshold of the lower kmer number (default = 0).")
parser.add_option("-L", "--low_boundary", dest="L", type="int", default=5, help="Input the lowest boundary of kmer number for the other bulk (default = 5).")
parser.add_option("-o", "--output", dest="o", help="Output file.")

(opt, args) = parser.parse_args()

# SET PARAMETERS AND FILES
f = open(opt.f)
t = opt.t 
L = opt.L
o = open(opt.o, "w")

# READ FILES AND SELECTION
header = f.readline()
o.write(header)
for line in f:
	line = line.split("\n")[0]
	ln = line.split("\t")
	b1 = int(ln[1])
	b2 = int(ln[2])
	if b1 <= t and b2 >= L:
		o.write(line+"\n")
	elif b2 <= t and b1 >= L:
		o.write(line+"\n")

o.close()
f.close()



