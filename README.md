# Characterize allelic and dosage variation in _Populus_ #

## Introduction ##
This repository includes all the data and scripts for CADVIP project.  

CADVIP (Characterize allelic and dosage variation in _Populus_) is the project for understanding the contribution of allelic variation and copy number variation on phenotypic outcomes in _Populus_.  

The initial _Populus_ population for this project was established and [published](https://pubmed.ncbi.nlm.nih.gov/26320226/) previously. Specifically, a wild-type egg cell from _Populus deltoides_ (female) is crossed with gamma-radiated pollen from _Populus nigra_ (male). Their F1 hybrids (~600 individuals) were collected and sent for Illumina short-read sequencing. The sequencing results indicate 52% of lines include large-scale deletions or insertions (indels) on the genome. The summary of these indels cover the 99% of _Populus_ genome. This becomes an excellent system for studying the interactive contribution of alleles and copy number states.  

To perform our experiment, we need both genotypes and phenotypes.  
1. Phenotypes are collected previously.  
2. Genotypes include two aspects: **Allele** and **Dosage**  
  **a. Allele**: The two crossing parents, both _P. deltoides_ and _P. nigra_, are outcrossing plants. We decide to investigate the alleles contributions from _P. deltoides_ and _P. nigra_ respectively.  
  **b. Dosage**: The dosage variation only occurred on _P. nigra_ (because of the gamma irradiation on pollen). We quantified the dosage variation and convert them into dosage genotypes.  

After the collection of phenotypes and genotypes, the data are imported into a customized QTL model to find out the contribution of each genetic aspect.  

## Allele ##
Our goal is to investigate the _P. deltoides_ alleles contribution and _P. nigra_ alleles contribution respectively. We followed the following steps for alleles extraction:  
**1. Haplotype phasing**  
**2. Genotyping**  

### Haplotype phasing ###
We aimed to get haplotypes for _P. deltoides_ and _P. nigra_. We would finally get two haplotype pairs:  
1. _P. deltoides_ 1 (D1) and _P. deltoides_ 2 (D2)  
2. _P. nigra_ 1 (N1) and _P. nigra_ 2 (N2)  

The working process is:  
1. Select the available SNPs for each parent haplotype.  
2. Use 122 RNA-seq F1 hybrids to phase the haplotype.  


#### SNPs selection ####
We get SNPs for _P. deltoides_ and _P. nigra_ respectively. The selected SNPs should be able to define which Haplotype does F1 hybrids inherited from the targeting parent. For example, if we are focusing on _P. nigra_ haplotypes, the available SNPs can be:  

|SNP.Name|M1    |M2      |F1    |F2     |Category        |
|:-------|:-----|:-------|:-----|:------|:---------------|
|SNP1    |A     |T       |A     |A      |M-Het+F-Homo    |
|SNP2    |A     |C       |A     |T      |M-Het+F-diffHet |
|SNP3    |A     |C       |G     |T      |M-Het+F-diffHet |

Similar selecting criteria can also be applied to _P. deltoides_.

The sequencing dataset for SNPs selection:
1. _P. deltoides_ and _P. nigra_ genomic sequencing data (Illumina paired-end sequencing, 45x read depth).

The programming process for SNPs selection:  
1. [Generate mpileup file](https://github.com/Comai-Lab/mpileup-tools).
  - Input: sorted.bam files for parental lines prepared for SNPs selection.  
  - Output: a parsed-mpileup file contains three parent lines: SO5465L (female1), SO5985L (female2), SO3615L (male1).  
2. [Select available SNPs](https://github.com/guoweier/CADVIP/blob/main/Phasing/scripts/SNP_3parents_4list.py)
  - Input: parsed-mpileup file from step1.
  - Output: Four lists:
    - List1: SO3615L-Homo/diffHet + SO5465L-Het.  
    - List2: SO3615L-Homo/diffHet + SO5985L-Het.  
    - List3: SO3615L-Het + SO5465L-Homo/diffHet.  
    - List4: SO3615L-Het + SO5985L-Homo/diffHet.  
  - Running example:  
  ```
  $ python SNP_3parents_4list.py -f parsed-mpileup-file.txt
  ```
  

#### Phasing ####
We used a subset of F1 lines (166/592) which contain RNA-seq dataset to decide the candidate haplotype combinations between adjacent SNPs.  


### Genotyping ###


## Dosage ##


## QTL ##

### RNA-seq samples ###

#### Genetic map construction ####

#### QTL analysis ####

##### Single variable #####

##### Multivariate #####

### F1 low-pass genomic data ###

#### Comfirmation of genotypes ####

#### QTL analysis ####
