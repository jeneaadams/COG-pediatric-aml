## 1) Convert BAM to VCF with GATK 
### Input :
BAM 

### Tool :
[GATK4 for RNAseq](https://github.com/gatk-workflows/gatk4-rnaseq-germline-snps-indels)

Workflows for processing RNA data for germline short variant discovery with GATK v4 and related tools

#### Requirements/expectations :
 - uBAM 

### Output :
 - A BAM file and its index.
 - A VCF file and its index. 
 - A Filtered VCF file and its index. 


## 2) Filtering (calls on mutations) 

??? 


## 3) Ancestry inference from VCF files 
### PLINK to convert .VCF --> .BED files 
```plink —vcf [filename] —double-id —make-bed —out [output filename]```

- [BED file documentation](https://zzz.bwh.harvard.edu/plink/binary.shtml)

### ADMIXTURE 



### PCA 
#### EIGENSTRAT


