
#this is code used to extract the psi values from each of the splicing events

#events_list = ("SE.MATS.JC.txt", "MXE.MATS.JC.txt", "A3SS.MATS.JC.txt", "A5SS.MATS.JC.txt", "RI.MATS.JC.txt")

import re 

def main():

    events_list = ("SE", "MXE", "A3SS", "A5SS", "RI")
    count = 0

    for event in events_list:
        #If SE
        if event == "SE":
            print "CURRENT EVENT: ", event
            f = open('SE.MATS.JC.txt', 'r')
            g = open('SE.MATS.JCEC.txt', 'r')
            header = f.readline()
            fout = open('SE.MATS.JC_PSI.txt', 'w')
            gout = open('SE.MATS.JCEC_PSI.txt', 'w')
            fout.write('ID\tPC3E_rep1\tPC3E_rep2\tPC3E_rep3\tGS689_rep1\tGS689_rep2\tGS689_rep3\n')
            gout.write('ID\tPC3E_rep1\tPC3E_rep2\tPC3E_rep3\tGS689_rep1\tGS689_rep2\tGS689_rep3\n')
            for line in f:
                ID, GeneID, geneSymbol, chrom, strand, exonStart_0base, exonEnd, upstreamES, upstreamEE, downstreamES, downstreamEE, ID, IJC_SAMPLE_1, SJC_SAMPLE_1, IJC_SAMPLE_2, SJC_SAMPLE_2, IncFormLen, SkipFormLen, PValue, FDR, IncLevel1, IncLevel2, IncLevelDifference = line.strip().split('\t')
                PSI = IncLevel1.split(',') + IncLevel2.split(',')
                if count == 0: 
                    print("PSI", event, PSI)
                    count +=1
                
                uniqID = chrom + ':' + exonStart_0base + '-' + exonEnd + '|' + strand + '|' + upstreamEE + '|' + downstreamES
		                

                fout.write(uniqID + '\t' + '\t'.join(PSI) + '\n')


            for line in g:
                ID, GeneID, geneSymbol, chrom, strand, exonStart_0base, exonEnd, upstreamES, upstreamEE, downstreamES, downstreamEE, ID, IJC_SAMPLE_1, SJC_SAMPLE_1, IJC_SAMPLE_2, SJC_SAMPLE_2, IncFormLen, SkipFormLen, PValue, FDR, IncLevel1, IncLevel2, IncLevelDifference = line.strip().split('\t')
                PSI = IncLevel1.split(',') + IncLevel2.split(',')

                
                uniqID = chrom + ':' + exonStart_0base + '-' + exonEnd + '|' + strand + '|' + upstreamEE + '|' + downstreamES
                
                gout.write(uniqID + '\t' + '\t'.join(PSI) + '\n')
            
            f.close()
            g.close()
            fout.close()
            gout.close()

            print("\t\tCompleted SE \n\n")

        

        #if MXE
        if event == "MXE":
            print "CURRENT EVENT: ", event
            f = open('MXE.MATS.JC.txt', 'r')
            g = open('MXE.MATS.JCEC.txt', 'r')
            header = f.readline()
            fout = open('MXE.MATS.JC_PSI.txt', 'w')
            gout = open('MXE.MATS.JCEC_PSI.txt', 'w')
            fout.write('ID\tPC3E_rep1\tPC3E_rep2\tPC3E_rep3\tGS689_rep1\tGS689_rep2\tGS689_rep3\n')
            gout.write('ID\tPC3E_rep1\tPC3E_rep2\tPC3E_rep3\tGS689_rep1\tGS689_rep2\tGS689_rep3\n')
            
            for line in f:
                ID, GeneID, geneSymbol, chrom, strand, firstExonStart_0base, firstExonEnd, secondExonStart_0base, secondExonEnd, upstreamES, upstreamEE, downstreamES, downstreamEE, ID, IJC_SAMPLE_1, SJC_SAMPLE_1, IJC_SAMPLE_2, SJC_SAMPLE_2, IncFormLen, SkipFormLen, PValue, FDR, IncLevel1, IncLevel2, IncLevelDifference = line.strip().split('\t')
                PSI = IncLevel1.split(',') + IncLevel2.split(',')
                # PSI = zip(IncLevel1.split(',') + IncLevel2.split(','))
                # if count == 0: 
                #     print("PSI", event, PSI)
                #     count +=1
                
                uniqID = chrom + ':'+ firstExonStart_0base + "-"+ firstExonEnd + ":" + secondExonStart_0base + "-" + secondExonEnd +'|'+ strand +'|'+ upstreamEE +'|'+ downstreamES
                # print("PSI", type(PSI))
                # print("uniqID", type(uniqID))
                fout.write(''.join(uniqID) + '\t' + '\t'.join(PSI) + '\n')
                # gout.write(uniqID + '\t' + '\t'.join(PSI) + '\n')
                
                
            for line in g: 
                ID, GeneID, geneSymbol, chrom, strand, firstExonStart_0base, firstExonEnd, secondExonStart_0base, secondExonEnd, upstreamES, upstreamEE, downstreamES, downstreamEE, ID, IJC_SAMPLE_1, SJC_SAMPLE_1, IJC_SAMPLE_2, SJC_SAMPLE_2, IncFormLen, SkipFormLen, PValue, FDR, IncLevel1, IncLevel2, IncLevelDifference = line.strip().split('\t')
                PSI = IncLevel1.split(',') + IncLevel2.split(',')
                # PSI = zip(IncLevel1.split(',') + IncLevel2.split(','))
                
                uniqID = chrom + ':'+ firstExonStart_0base + "-"+ firstExonEnd + ":" + secondExonStart_0base + "-" + secondExonEnd +'|'+ strand+'|'+ upstreamEE +'|'+ downstreamES
                
                # gout.write(uniqID + '\t' + '\t'.join(PSI) + '\n')
                gout.write(''.join(uniqID) + '\t' + '\t'.join(PSI) + '\n')

            f.close()
            g.close()
            fout.close()
            gout.close()

            print("Completed MXE\n\n")



        #if RI 
        if event == "RI":
            print "CURRENT EVENT: ", event
            f = open('RI.MATS.JC.txt', 'r')
            g = open('RI.MATS.JCEC.txt', 'r')
            header = f.readline()
            fout = open('RI.MATS.JC_PSI.txt', 'w')
            gout = open('RI.MATS.JCEC_PSI.txt', 'w')
            fout.write('ID\tPC3E_rep1\tPC3E_rep2\tPC3E_rep3\tGS689_rep1\tGS689_rep2\tGS689_rep3\n')
            gout.write('ID\tPC3E_rep1\tPC3E_rep2\tPC3E_rep3\tGS689_rep1\tGS689_rep2\tGS689_rep3\n')

            for line in f:
                ID, GeneID, geneSymbol, chrom, strand, riExonStart_0base, riExonEnd, upstreamES, upstreamEE, downstreamES, downstreamEE, ID, IJC_SAMPLE_1, SJC_SAMPLE_1, IJC_SAMPLE_2, SJC_SAMPLE_2, IncFormLen, SkipFormLen, PValue, FDR, IncLevel1, IncLevel2, IncLevelDifference = line.strip().split('\t')
                PSI = IncLevel1.split(',') + IncLevel2.split(',')

                uniqID = chrom + ':'+ upstreamEE + "-"+ downstreamES + ":" + strand+'|'+ upstreamES +'|'+ downstreamEE
                
                fout.write(''.join(uniqID) + '\t' + '\t'.join(PSI) + '\n')
                # gout.write(uniqID + '\t' + '\t'.join(PSI) + '\n')
                
            for line in g: 
                ID, GeneID, geneSymbol, chrom, strand, riExonStart_0base, riExonEnd, upstreamES, upstreamEE, downstreamES, downstreamEE, ID, IJC_SAMPLE_1, SJC_SAMPLE_1, IJC_SAMPLE_2, SJC_SAMPLE_2, IncFormLen, SkipFormLen, PValue, FDR, IncLevel1, IncLevel2, IncLevelDifference = line.strip().split('\t')
                PSI = IncLevel1.split(',') + IncLevel2.split(',')

                uniqID = chrom + ':'+ upstreamEE + "-"+ downstreamES + ":" + strand +'|'+ upstreamES +'|'+ downstreamEE
                
                gout.write(''.join(uniqID) + '\t' + '\t'.join(PSI) + '\n')

            f.close()
            g.close()
            fout.close()
            gout.close()

            print("Completed RI\n\n")



        #A3SS
        if event == "A3SS":
            print "CURRENT EVENT: ", event
            f = open("A3SS.MATS.JC.txt", 'r')
            g = open('A3SS.MATS.JCEC.txt', 'r')
            header = f.readline()
            fout = open('A3SS.MATS.JC_PSI.txt', 'w')
            gout = open('A3SS.MATS.JCEC_PSI.txt', 'w')
            fout.write('ID\tPC3E_rep1\tPC3E_rep2\tPC3E_rep3\tGS689_rep1\tGS689_rep2\tGS689_rep3\n')
            gout.write('ID\tPC3E_rep1\tPC3E_rep2\tPC3E_rep3\tGS689_rep1\tGS689_rep2\tGS689_rep3\n')


            for line in f:

                ID, GeneID, geneSymbol, chrom, strand, longExonStart_0base, longExonEnd, shortES, shortEE, flankingES, flankingEE, ID, IJC_SAMPLE_1, SJC_SAMPLE_1, IJC_SAMPLE_2, SJC_SAMPLE_2, IncFormLen, SkipFormLen, PValue, FDR, IncLevel1, IncLevel2, IncLevelDifference = line.strip().split('\t')
                PSI = IncLevel1.split(',') + IncLevel2.split(',')

                uniqID = chrom + ":" + flankingES + "-" + flankingEE +'|'+ strand +'|'+ longExonStart_0base +'|'+ shortES

                fout.write(''.join(uniqID) + '\t' + '\t'.join(PSI) + '\n')
                # gout.write(uniqID + '\t' + '\t'.join(PSI) + '\n')

            for line in g: 
                ID, GeneID, geneSymbol, chrom, strand, longExonStart_0base, longExonEnd, shortES, shortEE, flankingES, flankingEE, ID, IJC_SAMPLE_1, SJC_SAMPLE_1, IJC_SAMPLE_2, SJC_SAMPLE_2, IncFormLen, SkipFormLen, PValue, FDR, IncLevel1, IncLevel2, IncLevelDifference = line.strip().split('\t')
                PSI = IncLevel1.split(',') + IncLevel2.split(',')

                uniqID = chrom + ":" + flankingES + "-" + flankingEE +'|'+ strand +'|'+ longExonStart_0base +'|'+ shortES

                gout.write(''.join(uniqID) + '\t' + '\t'.join(PSI) + '\n')
                


            f.close()
            g.close()
            fout.close()
            gout.close()

            print("Completed A3SS \n\n")


        #A5SS
        if event == "A5SS":
            print "CURRENT EVENT: ", event
            f = open("A5SS.MATS.JC.txt", 'r')
            g = open('A5SS.MATS.JCEC.txt', 'r')
            header = f.readline()
            fout = open('A5SS.MATS.JC_PSI.txt', 'w')
            gout = open('A5SS.MATS.JCEC_PSI.txt', 'w')
            fout.write('ID\tPC3E_rep1\tPC3E_rep2\tPC3E_rep3\tGS689_rep1\tGS689_rep2\tGS689_rep3\n')
            gout.write('ID\tPC3E_rep1\tPC3E_rep2\tPC3E_rep3\tGS689_rep1\tGS689_rep2\tGS689_rep3\n')


            for line in f:

                ID, GeneID, geneSymbol, chrom, strand, longExonStart_0base, longExonEnd, shortES, shortEE, flankingES, flankingEE, ID, IJC_SAMPLE_1, SJC_SAMPLE_1, IJC_SAMPLE_2, SJC_SAMPLE_2, IncFormLen, SkipFormLen, PValue, FDR, IncLevel1, IncLevel2, IncLevelDifference = line.strip().split('\t')
                PSI = IncLevel1.split(',') + IncLevel2.split(',')

                uniqID = chrom + ":" + flankingES + "-" + flankingEE +'|'+ strand +'|'+ longExonStart_0base +'|'+ shortES

                fout.write(''.join(uniqID) + '\t' + '\t'.join(PSI) + '\n')
                # gout.write(uniqID + '\t' + '\t'.join(PSI) + '\n')

            for lin in g: 
                ID, GeneID, geneSymbol, chrom, strand, longExonStart_0base, longExonEnd, shortES, shortEE, flankingES, flankingEE, ID, IJC_SAMPLE_1, SJC_SAMPLE_1, IJC_SAMPLE_2, SJC_SAMPLE_2, IncFormLen, SkipFormLen, PValue, FDR, IncLevel1, IncLevel2, IncLevelDifference = line.strip().split('\t')
                PSI = IncLevel1.split(',') + IncLevel2.split(',')

                uniqID = chrom + ":" + flankingES + "-" + flankingEE +'|'+ strand +'|'+ longExonStart_0base +'|'+ shortES

                fout.write(''.join(uniqID) + '\t' + '\t'.join(PSI) + '\n')


            f.close()
            g.close()
            fout.close()
            gout.close()

            print("Completed A5SS \n\n") 
        
    
if __name__ == "__main__":
    main()
