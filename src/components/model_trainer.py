from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os, sys
from src.config.configuration import *
from dataclasses import dataclass
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
from src.utils import evaluate_model,save_obj # type: ignore

from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = MODEL_FILE_PATH
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_training(self,train_array,test_array):
        try:
            X_train,y_train,X_test,y_test = (train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1])

            models={
                'SVR':SVR(),
                'RandomForestRegressor':RandomForestRegressor(),
                "GradientBoostingRegressor":GradientBoostingRegressor(),
                "DecisionTreeRegressor":DecisionTreeRegressor(),
                "XGBRegressor":XGBRegressor()
            }

            model_report: dict = evaluate_model(X_train,y_train,X_test,y_test,models) 
            print(model_report)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = None

            for model_name, score in model_report.items():
                if score == best_model_score:
                    best_model_name = model_name
                    break

            if best_model_name is not None:
                print(f"Best Model Found, Model Name: {best_model_name}, R2 Score: {best_model_score}")
                logging.info(f"Best Model Found, Model Name: {best_model_name}, R2 Score: {best_model_score}")
                best_model = models[best_model_name]
                save_obj(file_path=self.model_trainer_config.trained_model_file_path, obj=best_model)
            else:
                print("No best model found.")
                logging.info("No best model found.")

        except Exception as e:
            raise CustomException(e,sys) #type:ignore