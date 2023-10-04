# Get your API token

Log into the cavatica website and click: Developer -> Authentication token

# Create a config file

Put the file at ~/.sevenbridges/credentials

📝 *Make sure this directory is in /home/adamsj8 (or other folder, not in a shared filesystem).* 

It should have these 3 lines:

[default]

api_endpoint = https://cavatica-api.sbgenomics.com/v2

auth_token = token_value

where token_value is your API token copied from the website

# install the python tools

Make a new directory on the HPC for the install and run these commands:

cd {new_directory}

conda create --prefix ./conda_env

conda activate ./conda_env

conda install -c conda-forge -c bioconda python=3

pip install git+https://github.com/kids-first/kf-cavatica-python-tools.git

git clone https://github.com/kids-first/kf-cavatica-python-tools.git

# Download files with the API

Run these commands

cd {the_directory_from_the_install}

``` cd /mnt/isilon/xing_lab/aspera/adamsj/kf_python_api ```

conda activate ./conda_env

``conda activate ./cavatica-api-env``

python ./kf-cavatica-python-tools/recipes/download_files.py --project_name {your_project_name} --project_path {rel_path/within/project} --download_location {path/to/store/downloaded/files}

``` python ./kf-cavatica-python-tools/recipes/download_files.py --project_name rmats_app_dev_JA --project_path bam_files --download_location /mnt/isilon/xing_lab/aspera/adamsj/kfAML_BAMs  ```

``python ./kf-cavatica-python-tools/recipes/download_files.py --project_name COG_analysis --project_path 2023OCT2_rmats-post --download_location /mnt/isilon/xing_lab/aspera/adamsj/COG_rmats_out/2023OCT2_rmats-post``

# More API info

* https://github.com/kids-first/kf-cavatica-python-tools
* https://sevenbridges-python.readthedocs.io/en/latest/quickstart/
