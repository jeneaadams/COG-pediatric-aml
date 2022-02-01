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

- use [VCFtools](http://vcftools.sourceforge.net/man_latest.html) to remove indel sites from the original VCF 

```vcftools --vcf input_file.vcf --remove-indels --recode --recode-INFO-all --out SNPs_only```


## 3) Ancestry inference from VCF files 
### PLINK to convert .VCF --> .BED files 
```plink —vcf [filename] —double-id —make-bed —out [output filename]```

[BED file documentation](https://zzz.bwh.harvard.edu/plink/binary.shtml)


### 3a. ADMIXTURE
[ADMIXTURE manual](https://dalexander.github.io/admixture/admixture-manual.pdf) 


#### input command with files: 
```admixture [BED_FILE.bed] [K] ```

Where K is the estimated number of Ancestral populations

There is an output file for each parameter set: Q (the ancestry fractions), and P (the allele frequencies of the inferred ancestral populations). Note that the output filenames have ‘3’ in them. This indicates the number of populations (K) that was assumed for the analysis. This filename convention makes it easy to run analyses using different values of K in the same directory.

- Choosing K 
    - Use ADMIXTURE’s cross-validation procedure. A good value of K will exhibit a low cross-validation error compared to other K values. Cross-validation is enabled by simply adding the --cv flag to the ADMIXTURE command line. In this default setting, the cross-validation procedure will perform 5-fold CV—you can get 10-fold CV, for example, using --cv=10. The cross-validation error is reported in the output. For example, if in our bash shell we ran 

    ``` for K in 1 2 3 4 5; \ do admixture --cv hapmap3.bed $K | tee log${K}.out; done```
    
    View CV erros: 
    
    ```grep -h CV log*.out```
    
    ![image](https://user-images.githubusercontent.com/54278292/151911733-9dbbb0e8-669c-4b49-95f6-6bd8744c2bb5.png)



### 3b. PCA 
#### [EIGENSTRAT --> EIGENSOFT](https://github.com/DReichLab/EIG)

Software [download](https://alkesgroup.broadinstitute.org/EIGENSOFT/) 

The EIGENSOFT package combines functionality from our population genetics methods (Patterson et al. 2006) and our EIGENSTRAT stratification correction method (Price et al. 2006). The EIGENSTRAT method uses principal components analysis to explicitly model ancestry differences between cases and controls along continuous axes of variation; the resulting correction is specific to a candidate marker’s variation in frequency across ancestral populations, minimizing spurious associations while maximizing power to detect true associations. The EIGENSOFT package has a built-in plotting script and supports multiple file formats and quantitative phenotypes.
* The latest EIGENSOFT(EIG) version is available [here](here) and on [the Alkes Price lab website](http://www.hsph.harvard.edu/alkes-price/software/).
**The EIGENSOFT FAQ is available [here](http://www.hsph.harvard.edu/alkes-price/eigensoft-frequently-asked-questions/). 




