# Weier Guo Python
# 01/08/2023 create

#### INTRODUCTION ####
# This script is to rename the sparsed common marker list into continued common marker list by filling the gap between sparsed markers.
# The allele information is not changed. 

import os, sys, math
from optparse import OptionParser
import itertools
from collections import OrderedDict

usage = ""
parser = OptionParser(usage=usage)
parser.add_option("-f", "--input_file", dest="f", help="Input genotype file with common marker list.")
parser.add_option("-g", "--genome_size", dest="g", help="Input file of each chromosome size.")
parser.add_option("-o", "--output", dest="o", help="Output file.")

(opt, args) = parser.parse_args()


#### FUNCTION AND PARAMETER DEFINE ####
# define parameters
f = open(opt.f,"r") 
g = open(opt.g,"r") 
o = open(opt.o,"w")
Ori_mk = OrderedDict()		# dictionary for original markers
Genome_mk = {}				# dictionary for all markers
Genomes = OrderedDict()		# dictionary for each chromosome size

# define pairwise() function
def pairwise(iterable):
	a,b = itertools.tee(iterable)
	next(b, None)
	return zip(a,b)


#### PROCESSING ####
# adjust each chromosome size
for line in g:
	if line[0] == "C":
		line = line.split("\n")[0]
		ln = line.split("\t")
		c = int(ln[0][3:])
		Genomes[c] = ln[1]

# extract marker names by reading the file head
head = f.readline()
head = head.split("\n")[0]
hd = head.split("\t")[1:]

# separate original markers by chromosome
for marker in hd:
	chrom = int(marker.split("_")[0][3:])
	if chrom not in Ori_mk:
		Ori_mk[chrom] = []
	Ori_mk[chrom] += [marker]

# get adjacent new markers
mpair = pairwise(hd)	# get paired markers
for item in mpair:
	m1 = item[0]				# get marker1
	m2 = item[1]				# get marker2
	chr1 = m1.split("_")[0]		# get chr for marker1
	chr2 = m2.split("_")[0]		# get chr for marker2
	start1 = m1.split("_")[1]	# get start pos for marker1
	start2 = m2.split("_")[1]	# get start pos for marker2
	end1 = m1.split("_")[2]		# get end pos for marker1
	end2 = m2.split("_")[2]		# get end pos for marker2

	if chr1 != chr2:
		continue
	else:
		if int(chr1[3:]) not in Genome_mk:
			Genome_mk[int(chr1[3:])] = []
			str_marker = chr1+"_"+"1"+"_"+str(int(start2)-1)
			Genome_mk[int(chr1[3:])] += [str_marker]
		else:
			marker = chr1+"_"+start1+"_"+str(int(start2)-1)
			Genome_mk[int(chr1[3:])] += [marker]

# add the last marker for each chromosome
for key in Genome_mk:
	emark_chr = Genome_mk[key][-1].split("_")[0]
	emark_str = str(int(Ori_mk[key][-1].split("_")[2])+1)
	emark_end = Genomes[key]
	end_marker = emark_chr+"_"+emark_str+"_"+emark_end
	Genome_mk[key] += [end_marker]

# sort markers in each chromosome
Genome_mk = OrderedDict(sorted(Genome_mk.items()))
for key in Genome_mk:
	Genome_mk[key].sort(key = lambda m: int(m.split("_")[1]))

### OUTPUT ####
# write the title for output file
ohead = "Old.Name"
for key in Genome_mk:
	for marker in Genome_mk[key]:
		ohead += "\t"+marker
o.write(ohead+"\n")

# write the rest of the lines in the file
for line in f:
	o.write(line)


f.close()
g.close()
o.close()








