# Weier Guo Python
# 09/20/2022

# Introduction
# The general goal is to compare between my QTLs and Heloise dQTLs. 
# This script is Step 1: Take the selected QTLs from my analysis, combined markers that are adjacent and have the same adjusted P-value. 

import os, sys, math
from optparse import OptionParser

usage = ""
parser = OptionParser(usage=usage)
parser.add_option("-f", "--input_file", dest="f", help="Genetic map file with markers physical position.")
parser.add_option("-g", "--genome_size", dest="g", help="Input file of each chromosome size.")
parser.add_option("-o", "--output", dest="o", help="Output file.")

(opt, args) = parser.parse_args()



