# Weier Guo Shell Scripting
# 08/03/2022

### Introduction ###
# Combine seq files in the bulk list.

mkdir depth2 
samples="POP28_22 POP30_21 POP25_80 POP28_64 POP28_80 POP26_37 POP26_23 POP31_68 POP25_73 POP28_44 POP29_07 POP28_50 POP26_81 POP31_60 POP25_54 POP28_23 POP26_63 POP25_09 POP29_89 POP31_17 POP28_59 POP29_35 POP30_64 POP28_28 POP28_88 POP28_81 POP25_74 POP25_40 POP27_88 POP30_92 POP26_74 POP28_83 POP28_27"

for dir in $samples
do 
	echo $dir 
	cat $dir/${dir}_CKDL220015007-1A_H3GL3DSX5_L2_1.fq.gz $dir/${dir}_CKDL220015007-1A_H3GL3DSX5_L2_2.fq.gz > ${dir}.fq.gz 
	mv ${dir}.fq.gz depth2/
done



