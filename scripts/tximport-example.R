library(tximport); library(readr); library(rhdf5)
tx2gene = read.table(file = fn_tx2gene, header = T, sep = '\t', quote = "")
tx2gene[,1] = gsub("\\..*", "", tx2gene[,1]) # resolve a problem "None of the transcripts in the quantification files are present in the first column of tx2gene."

txi <- tximport(files = file_vec, type="kallisto", tx2gene=tx2gene, ignoreTxVersion = TRUE, ignoreAfterBar = TRUE)

# build col data for txi
library(DESeq2)
coldata = data.frame(
    row.names = file_vec,
    condition = c(rep(conditions[1], length(group1)),
                  rep(conditions[2], length(group2))))

dds <- DESeqDataSetFromTximport(txi = txi,
                                colData = coldata,
                                design= ~ condition)
# dds <- collapseReplicates(dds, groupby = dds$replica) #collapsing technical replicates

# differential analysis
de <- DESeq(dds)
res = data.frame(results(de, contrast = c('condition', conditions[1], conditions[2])))
