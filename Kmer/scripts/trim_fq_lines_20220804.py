# Weier Guo Python
# 08/04/2022

### Introduction ###
# Trim .fq files to have similar reads depth for the two bulks. 


import os, sys, math
from optparse import OptionParser
import numpy as np 

usage = ""
parser = OptionParser(usage=usage)
parser.add_option("-f", "--input", dest="f", help="Input fq file.")
parser.add_option("-l", "--ori_line", dest="l", type="int", help="Input original liens.")
parser.add_option("-r", "--remained", dest="r", type="int", help="Input intended remained lines.")
parser.add_option("-o", "--output", dest="o", help="Output file.")

(opt, args) = parser.parse_args()

### SET PARAMETERS AND FILES ###
f = open(opt.f,"r")
ori_line = [j for j in range(0,opt.l,4)]	# record the read name line number for each sequencing read
r = opt.r // 4						# the number of reads for keeping		
o = open(opt.o,"w")

# to shorten the running time, every 25 reads set as a unit
# ori_line_100 = [j for j in range(0,len(ori_line),100)]
# r_100 = r // 100

### READS GOING TO KEEP BY RANDOMIZATION ###
remained = list(np.random.choice(ori_line, r, replace=False))

### WRITE NEW FILE ###
# read all lines into list 
lines = f.readlines()
# write lines
for i in remained:
	for x in range(4):
		o.write(lines[i+x])

f.close()
o.close()
