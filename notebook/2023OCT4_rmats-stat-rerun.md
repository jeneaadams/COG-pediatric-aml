# Objective 
I am re-running rmats-turbo with stats off, them collectively with the stats mode on so that I can get a consensus estimate of the statistically significant splicing events BEFORE splitting the files into replicate groups. 

# Steps 
- [ ] Run rmats prep on Cavatica
- [ ] Run rmats post on Cavatica
- [ ] Download the post output to ``/mnt/isilon/xing_lab/aspera/adamsj/COG_rmats_out/2023OCT2_rmats-post/2023OCT2_rmats-post/``
- [ ] Run rMATS ``task --stat`` on the output
- [ ] For next comparison (NPM mutation status) extract bam files and run filtering
- [ ] compare significant splicing event counts between old and new approach
- [ ] Move forward with NPM analysis 
  - [ ] run SPARK to look at RBPs involved with signififanct splicing events
  - [ ] Gene expression analysis
  - [ ] 
