# Weier Guo Shell Scripting
# 08/25/2022

# Introduction
# Jellyfish count + dump with two bulks in Populus

phenos="width depth mvd"
bulks="1 2"

for pheno in $phenos
do 
	echo $pheno
	if [ $pheno == width ]
	then 
		for bulk in $bulks
		do 
			echo $bulk
			# jellyfish count <(zcat ${pheno}${bulk}.fq.gz) -C -m 21 -t 10 -s 1G -o ${pheno}${bulk}_21.jf
			jellyfish dump -L 5 -c -t ${pheno}${bulk}_21.jf > ${pheno}${bulk}_21.fa
		done
	else
		for bulk in $bulks
		do 
			echo $bulk
			# jellyfish count <(zcat ${pheno}${bulk}.fq.gz) -C -m 31 -t 10 -s 1G -o ${pheno}${bulk}_31.jf
			jellyfish dump -L 5 -c -t ${pheno}${bulk}_31.jf > ${pheno}${bulk}_31.fa
		done
	fi
done

