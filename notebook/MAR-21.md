
# After STAR alignment from fastq files 
1. Locate BAM files 
a. May have to use something like this to get them all into one text file: 
	i. ls /mnt/isilon/xing_lab/aspera/TCGA/BAMs/TCGA_LAML/RL50/*/Aligned.sortedByCoord.out.bam | tr '\n' ',' | sed 's/,$//' > b1_TCGA.txt
	ii. ls /mnt/isilon/xing_lab/aspera/TCGA/BAMs/TARGET_AML/RL100/*/Aligned.sortedByCoord.out.bam | tr '\n' ',' | sed 's/,$//' > b1_TARGET.txt
b. Make sure the bam.txt files re in the directory you want to run the rMATS-turbo code in 
2. Add bam fils to b1 script 
a. If not using b2, make sure --statoff is flagged 
3. Run following qsub code to run prep and post steps of rmats-turbo 


	```#! /bin/bash
	#$ -S /bin/bash
	#$ -R y
	#$ -cwd
	#$ -V
	#$ -m ea
	#$ -M adamsj8@email.chop.edu
	#$ -j y
	#$ -l h_vmem=16G,m_mem_free=16G
	#$ -N rmats_TCGA_JA
	python2 /mnt/isilon/xing_lab/aspera/wangy14/rmats-turbo/rmats.py --gtf /mnt/isilon/xing_lab/aspera/wangy14/reference_genome/gencode.v31lift37.annotation.gtf --tmp prepTCGA --od postTCGA --readLength 101 --b1 b1_TCGA.txt -t paired --anchorLength 1 --nthread 1 --libType fr-unstranded --task both --variable-read-length --novelSS --statoff```


Post 
	
	```python2 /mnt/isilon/xing_lab/aspera/wangy14/rmats-turbo/rmats.py --gtf /mnt/isilon/xing_lab/aspera/wangy14/reference_genome/gencode.v31lift37.annotation.gtf --tmp prepTARGET --od postTARGET --readLength 101 --b1 TARGET_AML_bam.txt -t paired --anchorLength 1 --nthread 4 --libType fr-unstranded --task post --variable-read-length --novelSS --statoff```

• When separating into batches, need to run prep and post step separately

• Post step can only be run once 

- Post step input is the splicing graph which is the temp parameter 
	- Use same temp directory 
	- Only specify temp directory 
	- Write path of bam files in b1 or b2 --> only using path itself, not the bam file itself, its extracting the path to match it to the splicing graph files 


### 6/30 sbatch --mem=50G -c 4 qsub_prep_TCGA_JA_1.sh

4. A prep and post folder will be created (be sure to change the name if needed ) in the same directory you run the above code in 

5. The post directory will have rMATS output files 
	a. 
6. Filter the events with high confidence 

	
	
### 4/21 --> removed filtered files and try less stringent filtering 
7. Calculate PSI values
	a. In rMATS output directory run  psi_extract_JA.py to extract the psi values 
	b. The files with PSI values will be created in this directory 

8. Gene expression 
	a. Cufflinks or DESeq --> used as input for PEGASAS and 

9. Generate sashimi plot

	a. ```rmats2sashimiplot --b1 b1_to_4.txt -t SE --e ./postTCGA/filtered_SE.MATS.JC.txt --l1 SampleOne --exon_s 1 --intron_s 5 -o ./sashimi```
	
	b. ```rmats2sashimiplot --b1 b1_to_4.txt -t SE -e ./postTCGA/filtered_SE.MATS.JC.txt --l1 SampleOne --exon_s 1 --intron_s 5 -o ./sashimi```
	
	c. ```python /home/adamsj8/aspera/adamsj/TCGA_AML/postTCGA/rmats2sashimiplot/src/rmats2sashimiplot/rmats2sashimiplot_new.py --b1 b1_TCGA_1_ to_4.txt -t 	SE./postTCGA/filtered_SE.MATS.JC.txt --l1 SampleOne --exon_s 1 --intron_s 5 -o ./sashimi```

