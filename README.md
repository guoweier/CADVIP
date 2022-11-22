# CADVIP 
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

#### Phasing ####


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
