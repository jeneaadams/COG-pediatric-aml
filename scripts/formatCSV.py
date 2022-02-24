
## Jenea Adams


# import csv

import pandas as pd
from termcolor import colored


def main():
    # f = open('_2_aggregated.csv')
    #
    # csv_f = csv.reader(f)
    #
    # cols = len(next(csv_f))
    #
    # cols


    # input CSV
    df = pd.read_csv('_2_aggregated.csv', header=None)

    # output CSV

    #Index CSV file and create a list of the paths for reference
    columns = 0
    sample_list = []
    # for i in len(df.shape[1]):
    for index, row in df.iterrows():
        for cols in row:
            sample_list.append(cols)
            columns += 1

    # print(columns)

    # print(len(sample_list), '\n')

    # print(sample_list[1])


    # print(type(sample_list[1]
    #     # els = sample_list[1].split("/")
    #     # # print("\n\n els -1 \n", els[-1])
    #     #
    #     # bam_file = els[-1]
    #     # # print(bam_file)
    #     #
    #     # # print("\n -- bam_file.split")
    #     # bam_file_split = bam_file.split(".")
    #     #
    #     # # print("bam_file_split \n", bam_file_split)
    #     #
    #     # bam_name = bam_file_split[0]
    #     #
    #     # # print("\n bam_name\n", bam_name)))
    #


    new_bam_list = []

    # function for processing each path
    def path2BAM(inputPath):

        # processings the paths
        elements = sample_list[sample_list.index(inputPath)].split("/")
        bam_file = elements[-1]
        bam_file_split = bam_file.split(".")
        bam_name = bam_file_split[0]

        # adding the bam name to the csv
        df[inputPath] = bam_name


        print(colored(bam_name, "green"))
        print("\t\t\t\tCOMPLETE")

        #end function

    # path2BAM("/sbgenomics/Projects/60da54a2-bba2-4075-9fee-8cb904f7497b/aligned-reads/3554e8cd-50cb-49bc-9ccb-d93b473d3eb0.Aligned.out.sorted.bam")


    #test
    for i in range(0,100):
        curr_path = sample_list[i]
        path2BAM(curr_path)

    print(df.iloc[0])




if __name__ == '__main__':
    main()
