# This file is used to declare all the constant variable to be used in code to create paths and file names.

import os, sys
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()

ROOT_DIR_KEY = os.getcwd() #Store the path of Current working directory

DATA_DIR ="Data" # Directory in which csv file is present
DATA_DIR_KEY = "data.csv" #Actual file

# Creating new Directory to store the downloaded data in client side

ARTIFACT_DIR_KEY = "Artifact" #Declaring a Directory in which the downloaded data will be stored 


# Data ingestion related variable used in Ingesting a data in the CLient side
#  all are variables 

DATA_INGESTION_KEY ="data_ingestion"  
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"

# It will create a directory like this 
# Artifact/data_ingestion/Date_time_name_folder/Ingested_dir->train,test data set
#                                                           -> raw data set 


# Data Transformation related variable

DATA_TRANSFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCESSED_DIR = "processor"
DATA_TRANSFORMATION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORM_DIR = "transformation"
TRANSFORM_TRAIN_DIR_KEY = "train.csv"
TRANSFORM_TEST_DIR_KEY = "test.csv"


