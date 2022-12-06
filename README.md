## DSC 180 Quarter 1 Project: Genetic Risk Prediction

The files in this repo:
- `data`: 
  - `raw`: contains 3 files of test data generated for the purpose of testing my code 
- `config`: contains 3 files each with the configurations needed for each different function in etl.py 
          to process the raw data and create the temp data 
  - `bed_config.json`: corresponds to /data/raw/test_subset.bed and is used to run /SRC/etl.py get_bed()
  - `bim_config.json`: corresponds to /data/raw/test_subset.bim and is used to run /SRC/etl.py get_bim()
  - `exp_config.json`: corresponds to /data/raw/test_sg.csv and is used to run /SRC/etl.py get_expressions()
- `SRC`: 
  - `etl.py`: contains functions that call test data from /data/raw and processes them for 
            function calls contained in eda.py 
  - `eda.py`: contains main functions to execute my reults. 
            - generate_regression() replicates the regression run on the data to produce the 
              figures used in my final report 
- `notebooks`: contains my final report in pdf format 
- `run.py`: the code that is executed upon calling python run.py 
- `submission.json`: contains the dockerhub image necessary to run all code within this notebook 
