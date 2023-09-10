from src.constants import *
import os, sys


# Creating folders to store all the data in it
ROOT_DIR = ROOT_DIR_KEY

# Dataset_url = 

DATASET_PATH = os.path.join(ROOT_DIR, DATA_DIR, DATA_DIR_KEY)
# This is the Dataset path C:\Users\Naren\source\repos\OneDrive\Desktop\GitHub\Ml-Project\src\config\Data\data.csv

print(DATASET_PATH)
RAW_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP, 
                             DATA_INGESTION_RAW_DATA_DIR, RAW_DATA_DIR_KEY)
# It will create a path like this for raw data C:\Users\Naren\source\repos\OneDrive\Desktop\GitHub\Ml-Project\src\config\Artifact\data_ingestion\2023-08-31 10-36-51\raw_data_dir\raw.csv



TRAIN_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP,
                               DATA_INGESTION_INGESTED_DATA_DIR_KEY, TRAIN_DATA_DIR_KEY)

# It will create a train.csv file to store train dataset C:\Users\Naren\source\repos\OneDrive\Desktop\GitHub\Ml-Project\src\config\Artifact\data_ingestion\2023-08-31 10-38-18\ingested_dir\train.csv


TEST_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP,
                               DATA_INGESTION_INGESTED_DATA_DIR_KEY, TEST_DATA_DIR_KEY)
# It will create a test.csv file to store test dataset C:\Users\Naren\source\repos\OneDrive\Desktop\GitHub\Ml-Project\src\config\Artifact\data_ingestion\2023-08-31 10-38-18\ingested_dir\test.csv



# Data Transformation steps


PREPROCESSING_OBJ_FILE = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_TRANSFORMATION_ARTIFACT, 
                                     DATA_PREPROCESSED_DIR, DATA_TRANSFORMATION_PROCESSING_OBJ)

TRANSFORM_TRAIn_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_TRANSFORMATION_ARTIFACT,
                                         DATA_TRANSFORM_DIR, TRANSFORM_TRAIN_DIR_KEY)


TRANSFORM_TEST_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_TRANSFORMATION_ARTIFACT,
                                         DATA_TRANSFORM_DIR, TRANSFORM_TEST_DIR_KEY)



FEATURE_ENGG_OBJ_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_TRANSFORMATION_ARTIFACT,
                                          DATA_PREPROCESSED_DIR,' feature_engg.pkl')