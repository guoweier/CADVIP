# Weier Guo Shell Scripting
# 08/29/2022

# find all files in current directory
files=$(ls ../Pvalue_Leaf_DelNig/)

# get file name for each file
for file in ${files}
do
	fname=$(echo $file | cut -d '.' -f 1)
	mv ../Pvalue_Leaf_DelNig/${fname}.csv ../Pvalue_Leaf_DelNig/${fname}_lm.csv
done