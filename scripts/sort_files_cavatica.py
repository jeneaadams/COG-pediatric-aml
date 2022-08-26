"""python script using the cavatica api to group certain  files into a specific folder in a cavatica project. 
Can be used to sort bam files from replicate groups into individual folders for downstream analysis with rmats2sashimimplot"""

import sevenbridges as sbg
import argparse
import pandas as pd
from kf_cavatica.projects import fetch_project
import os

from kf_cavatica.files import list_files_recursively
from pathlib import Path
from tqdm import tqdm
import os
import logging


# Arguments 
parser = argparse.ArgumentParser(
    prog="Find and group a list of bam file within a Cavatica files for processing with other tools like rmats2sashimiplot",
    description="""Find and group a list of bam file within a Cavatica""",
)

parser.add_argument( #mine is jiadams/cog-analysis
    "--project_id", 
    metavar="Cavatica project ID", 
    type=str, 
    help="""'Username/project_name' ID of the project in cavatica where the files come from.""",
)

parser.add_argument(
    "--project_name",
    metavar="Cavatica project name",
    type=str,
    help="""Name of the project in cavatica where the files come from.
            Note that a user may have multiple projects with the same name, so
            best practice is to reference entities by ID.\n
            See `--project_id`.
            """,
)

parser.add_argument(
    "--project_path",
    metavar="Path inside project to look for files to download",
    type=str,
    help="""Specify project path to download files in a certain folder within a
            cavatica project. If no project_path is given, download all files in
            a project.
            """,
)

parser.add_argument(
    "--new_folder_name", 
    metavar="Name of the folder that will be created to move the files to", 
    type=str,
    help="A new folder is created within the project and the files are moved here",
)

parser.add_argument(
    "--tag",
    metavar="How the new files should be labeled in the folder",
    type=str,
    help="this adds a descriptive tag or label to the files within the cavatica project for quick filtering downstream",
)

parser.add_argument(
    "--list", 
    metavar="The text list of files to search for in the Cavatcia porject", 
    type=str,
    help="The text list of files to search for in the Cavatcia porject",
)


args = parser.parse_args()
print(f"Args: {args.__dict__}")


#Connect to the API 
print("Connecting to API")

config_file = sbg.Config(profile="default")
api = sbg.Api(
    config=config_file,
    error_handlers=[
        sbg.http.error_handlers.rate_limit_sleeper,
        sbg.http.error_handlers.maintenance_sleeper,
    ],
)


#Generate project object
print("Generating project object")
project = api.projects.get(id=args.project_id)


print("Initiating file count")
file_count = 0


print("Creating new folder")
new_folder = api.files.create_folder(name=args.new_folder_name, project=args.project_id)


print("Reading text file list")
with open(args.list) as file_list:
    print("Sorting files...")
    for line in file_list:
        # file = api.files.get(project = project, names = line.strip()) #may need to modify project name in the future
        file = api.files.get(id = line.strip()) #may need to modify project name in the future

        file.tags = [args.tag]
        file.save()

        file.copy_to_folder(parent=new_folder) #left out name argument because I don't want to rename it
        file_count+=1


print(file_count, "files moved to", args.new_folder_name)

print("Closing file")
file_list.close()

print("DONE")