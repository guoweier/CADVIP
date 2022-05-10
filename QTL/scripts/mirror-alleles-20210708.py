from __future__ import division
import os, sys, math, time
from optparse import OptionParser
from collections import OrderedDict

# This script add mirror alleles for binned SNP markers for construct genetic maps. 
# To better organize the linkage groups, and also evaluate the phased haplotypes in poplar, we add mirror allele for each binned marker.
# Mirror alleles are the ones that flip AB order with the original ones. i.e, A -> B, B -> A
# Input: The genotype file with samples as the rows, and markers as the columns. Genotypes are denoted as A or B. NA represents no genotype information. 
# Output: 
# Sample M1a M2a M3a ... Mna M1b M2b M3b ... Mnb
# Both input and output files are .csv


usage = "\n\n%prog"
parser = OptionParser(usage=usage)

parser.add_option("-f", "--file", dest="f", help="Input genotype file")
parser.add_option("-o", "--outputfile", dest="o", help="Output file")

(opt, args) = parser.parse_args()

#input parameters
f = open(opt.f)
o = open(opt.o, "w")

#read file header
#add mirror allele names into output file
header = f.readline()
header = header.split("\n")[0]
hd = header.split(",")
ohead = hd[0]
for i in range(1,len(hd)):
	ohead += ","+hd[i]+"a"
for i in range(1,len(hd)):
	ohead += ","+hd[i]+"b"
o.write(ohead+"\n")

#read genotype file
for line in f:
	line = line.split("\n")[0]
	ln = line.split(",")
	text = ln[0]
	for i in range(1,len(ln)):
		text += ","+ln[i]
	for i in range(1,len(ln)):
		if ln[i] == "A":
			text += ",B"
		elif ln[i] == "B":
			text += ",A"
		elif ln[i] == "NA":
			text += ",NA"
	o.write(text+"\n")

f.close()
o.close()




