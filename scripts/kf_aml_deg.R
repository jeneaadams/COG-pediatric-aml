if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("TxDb.Hsapiens.UCSC.hg19.knownGene")

BiocManager::install("tximeta")

library(tximportData)


dir <- "/Users/adamsj8/Desktop/kallisto_output"
list.files(dir)

#create a named vector pointing to qunatification files 
samples <- read.csv(file.path(dir, "kf_aml_kallisto_metadata.csv"), header = TRUE)
samples

#associate transcript IDs with GENE IDs 
# BiocManager::install("TxDb.Hsapiens.UCSC.hg19.knownGene")
library(TxDb.Hsapiens.UCSC.hg19.knownGene)
txdb <- TxDb.Hsapiens.UCSC.hg19.knownGene
k <- keys(txdb, keytype = "TXNAME")
tx2gene <- select(txdb, k, "GENEID", "TXNAME")

##NEED A TABLE THAT CONTAINS SAMPLE IDs

files <- file.path("/Users/adamsj8/Desktop/kallisto_output", "kallisto", samples$case_id, "abundance.tsv")
names(files) <- paste0("sample", 1:6)
txi.kallisto.tsv <- tximport(files, type = "kallisto", tx2gene = tx2gene, ignoreAfterBar = TRUE)
head(txi.kallisto.tsv$counts)