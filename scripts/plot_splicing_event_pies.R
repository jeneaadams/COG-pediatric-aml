#!/usr/bin/env Rscript

# Author Jenea Adams; adapted from Yuanyuan Wang 
#  This script creates pie chart for splicing events between replicate groups from rMATS-turbo filtering output 

# Plot all splicing events
nSE <- system("cat /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/rmats_filtering/filtered_SE.MATS.JC.txt | wc -l ", intern = TRUE)
nA5SS <- system("cat /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/rmats_filtering/filtered_A5SS.MATS.JC.txt | wc -l ", intern = TRUE)
nA3SS <- system("cat /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/rmats_filtering/filtered_A3SS.MATS.JC.txt | wc -l ", intern = TRUE)
nMXE <- system("cat /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/rmats_filtering/filtered_MXE.MATS.JC.txt | wc -l ", intern = TRUE)
nRI <- system("cat /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/rmats_filtering/filtered_RI.MATS.JC.txt | wc -l ", intern = TRUE)

Prop <- c(SE = as.integer(nSE)-1, A5SS = as.integer(nA5SS)-1, A3SS = as.integer(nA3SS)-1, MXE = as.integer(nMXE)-1, RI = as.integer(nRI)-1)
labels <- paste0(names(Prop), ' ', format(Prop, big.mark = ','))

pie(Prop , labels = labels, clockwise = T, angle = 0)

pdf('/mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/rmats_filtering/plot_pie_filtered1.pdf', width = 4, height = 4)
pie(Prop , labels = labels, clockwise = T, angle = 0)
dev.off()



## PLotting significant events 
nSE <- system("cat /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/high-low/rmats_filtering_highlow/up_SE.MATS.JC.txt /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/high-low/rmats_filtering_highlow/dn_SE.MATS.JC.txt | wc -l ", intern = TRUE)
nA5SS <- system("cat /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/high-low/rmats_filtering_highlow/up_A5SS.MATS.JC.txt /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/high-low/rmats_filtering_highlow/dn_A5SS.MATS.JC.txt | wc -l ", intern = TRUE)
nA3SS <- system("cat /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/high-low/rmats_filtering_highlow/up_A3SS.MATS.JC.txt /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/high-low/rmats_filtering_highlow/dn_A3SS.MATS.JC.txt | wc -l ", intern = TRUE)
nMXE <- system("cat /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/high-low/rmats_filtering_highlow/up_MXE.MATS.JC.txt /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/high-low/rmats_filtering_highlow/dn_MXE.MATS.JC.txt | wc -l ", intern = TRUE)
nRI <- system("cat /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/high-low/rmats_filtering_highlow/up_RI.MATS.JC.txt /mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/high-low/rmats_filtering_highlow/dn_RI.MATS.JC.txt | wc -l ", intern = TRUE)


Prop <- c(SE = as.integer(nSE)-2, A5SS = as.integer(nA5SS)-2, A3SS = as.integer(nA3SS)-2, MXE = as.integer(nMXE)-2, RI = as.integer(nRI)-2)
labels <- paste0(names(Prop), ' ', format(Prop, big.mark = ','))

pie(Prop , labels = labels, clockwise = T, angle = 0)

pdf('/mnt/isilon/xing_lab/aspera/adamsj/post_output_kfAML/rmats_filtering/plot_pie_significant.pdf', width = 4, height = 4)
pie(Prop , labels = labels, clockwise = T, angle = 0)
dev.off()
