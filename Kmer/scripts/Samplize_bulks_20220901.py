# Weier Guo Python
# 09/01/2022

# Introduction: 
# Randomly select a sample from the k-mer bulk files. 
# The sample size (percentage) and sample number (recurrency) can be customized. 


import os, sys, math
from optparse import OptionParser
import numpy as np 

usage = ""
parser = OptionParser(usage=usage)
parser.add_option("-f", "--input", dest="f", help="Input bulk table.")
parser.add_option("-l", "--ori_line", dest="l", type="int", help="Input original lines.")
parser.add_option("-p", "--percent", dest="p", type="float", default=0.001, help="Input sample size percentage (default 0.001).")
parser.add_option("-r", "--recurrent", dest="r", type="int", default=1, help="Input the sample numbers (default 1).")
#parser.add_option("-o", "--output", dest="o", help="Output file.")

(opt, args) = parser.parse_args()


### SET PARAMETERS AND FILES ###
f = open(opt.f)
l = opt.l 
p = opt.p 
r = opt.r 
fname = opt.f
oname = fname.split(".")[0]

### RANDOMIZE THE SAMPLE LINE INDICES ###
samp_n = int(round(l * p, 0))
samp_i = list(np.random.choice(l, samp_n, replace=False))

### CREATE NEW FILES ###
# read input file 
lines = f.readlines()

# recurrently write output files 
for i in range(r):
	o = open(oname+"_"+str(p*100)+"%"+"_sample"+str(i+1)+".txt","w")
	for j in samp_i:
		o.write(lines[j])
	o.close()


f.close()










