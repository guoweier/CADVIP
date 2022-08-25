# Weier Guo Shell Scripting
# 08/17/2022

# Introduction
# Multiple running of jellyfish count + jellyfish histo. 

kmers="15 17 19 21 23 25 27 29 31"

for kmer in $kmers
do 
	echo $kmer 
	jellyfish count <(zcat mvd2.fq.gz) -C -m $kmer -t 10 -s 1G -o mvd2_${kmer}.jf
	jellyfish histo -t 10 mvd2_${kmer}.jf > mvd2_${kmer}.histo
done
