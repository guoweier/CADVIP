# Weier Guo Python
# Create: 12/14/2022

import os, sys, math
from optparse import OptionParser
import itertools
from collections import OrderedDict
import numpy as np

usage = ""
parser = OptionParser(usage=usage)
parser.add_option("-g", "--genotype_file", dest="g", help="Input genotype file.")
parser.add_option("-o", "--output", dest="o", help="Output file.")

(opt, args) = parser.parse_args()

## SET PARAMETERS AND FUNCTIONS ##
g_op = open(opt.g,"r")
o = open(opt.o,"w")
Chroms = {}			# dictionary includes the start and end columns for each chromosome

## GET START AND END LOCATIONS FOR EACH CHROMOSOME ##
header = g_op.readline()
header = header.split("\n")[0]
hd = header.split("\t")


# write header line for output file
o.write(header+"\n")

# convert genotype files to matrix
g = np.loadtxt(g_op, delimiter = "\t", dtype = str)
nrow, ncol = g.shape

# define pairwise() function
def pairwise(iterable):
	a,b = itertools.tee(iterable)
	next(b, None)
	return zip(a,b)

# get chromosome boundaries
for i in range(1,len(hd)):
	chrom = int(hd[i].split("_")[0][3:])
	if chrom not in Chroms:
		if chrom == 1:
			Chroms[chrom] = [1]
		else:
			Chroms[chrom-1] += [i-1]
			Chroms[chrom] = [i]
# add the end marker of chr19
Chroms[19] += [len(hd)-1]

# sort numbers in chrom dict 
Chroms = OrderedDict(sorted(Chroms.items()))

## IMPUTE GENOTYPE ##
for r in range(nrow):										# read each sample info
	old_name = g[r,0]
	text = old_name+"\t"
	Genotype = []
	for key in Chroms:										# get each chromosome 
		start = Chroms[key][0]
		end = Chroms[key][1]
		chr_ms = g[r,start:(end+1)]							# separate markers info by chromosomes
		chr_NAs_col = list(np.where(chr_ms=="NA")[0])		# extract NAs column number
		chr_NAs_pairs = list(pairwise(chr_NAs_col))			# get each NAs column distance


		
		NAs_group = []										# initial group for adjacent NA markers
		NAs_Groups = []										# final NA groups storage
		for pair in chr_NAs_pairs:
			if pair[1]-pair[0] == 1:						# if NAs are adjacent
				NAs_group = NAs_group + [pair[0],pair[1]]
				if pair == chr_NAs_pairs[-1]:
					NAs_group_uni = list(np.unique(NAs_group))
					NAs_Groups += [NAs_group_uni]
			elif pair[1]-pair[0] != 1:						# if NAs are not adjacent
				NAs_group.append(pair[0])
				NAs_group_uni = list(np.unique(NAs_group))
				NAs_Groups += [NAs_group_uni]
				NAs_group = [pair[1]]
				if pair == chr_NAs_pairs[-1]:
					NAs_group_uni = list(np.unique(NAs_group))
					NAs_Groups += [NAs_group_uni]

		# impute genotype with upward and downward genotypes
		for group in NAs_Groups:
			if group[0] == 0 and group[-1] == len(chr_ms)-1:
				continue
			elif group[0] == 0:
				downward = chr_ms[group[-1]+1]
				if downward != "0":
					for loc in group:
						chr_ms[loc] = downward
			elif group[-1] == len(chr_ms)-1:
				upward = chr_ms[group[0]-1]
				if upward != "0":
					for loc in group:
						chr_ms[loc] = upward
			else:
				upward = chr_ms[group[0]-1]
				downward = chr_ms[group[-1]+1]
				if upward == downward and upward != "0":		# equal 0 means is in Pnigra and is a deletion 
					for loc in group:
						chr_ms[loc] = upward

		# join chromosomes to genome
		Genotype = Genotype + list(chr_ms)
	
	# write sample line into output file
	text += "\t".join(Genotype)
	o.write(text+"\n")

g_op.close()
o.close()







