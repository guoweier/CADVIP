# Weier Guo Shell Scripting
# 08/17/2022

# Introduction
# Multiple running of jellyfish count + jellyfish histo. 

kmers="15 17 19 23 25 27 29"

for kmer in $kmers
do 
	echo $kmer 
	jellyfish count <(zcat width1.fq.gz) -C -m $kmer -t 10 -s 1G -o width1_${kmer}.jf
	jellyfish histo -t 10 width1_${kmer}.jf > width1_${kmer}.histo
done
