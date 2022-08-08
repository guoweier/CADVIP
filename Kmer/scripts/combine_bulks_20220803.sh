# Weier Guo Shell Scripting
# 08/03/2022

### Introduction ###
# Combine seq files in the bulk list.

mkdir mvd2 
samples="POP30_65 POP30_38 POP26_25 POP26_02 POP29_07 POP27_81 POP30_33_POP26_33 POP27_11 POP28_29 POP25_23 POP31_19 POP27_41 POP27_38 POP25_42 POP25_24 POP28_70 POP29_63 POP25_85 POP28_73 POP27_35 POP26_07_POP30_07 POP27_24 POP26_80 POP28_79 POP29_15 POP29_56 POP28_36 POP29_01 POP28_24"

for dir in $samples
do 
	echo $dir 
	cat $dir/${dir}_CKDL220015007-1A_H3GL3DSX5_L2_1.fq.gz $dir/${dir}_CKDL220015007-1A_H3GL3DSX5_L2_2.fq.gz > ${dir}.fq.gz 
	mv ${dir}.fq.gz mvd2/
done



