# Here, we'd be writing modular codes solely for the purpose of predicting unseen data 

import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
from dataclasses import dataclass

from src.components.data_transformation import DataTransform
from src.components.model_trainer import ModelTrainer

@dataclass
class DataChannel:
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    reading_score: int
    writing_score: int

    def switch_to_df(self):
        try:
            logging.info('Inputted has been retrieved, about to be transformed')
            input_data_dict = {
                'gender': [self.gender],
                'race/ethnicity': [self.race_ethnicity],
                'parental level of education': [self.parental_level_of_education],
                'lunch': [self.lunch],
                'test preparation course': [self.test_preparation_course],
                'reading score': [self.reading_score],
                'writing score': [self.writing_score]
            }
            # The keys in 'input_data_dict' MUST correspond with the column labels of the originally trained data
            logging.info('Inputted data has been transformed')
            return pd.DataFrame(input_data_dict)

        except Exception as e:
            raise CustomException(e,sys)
        
def predict(df: pd.DataFrame):
    try:
        logging.info('Estimator and Preprocessor obj has been called, into which the inputted data is fed')
        estimator_path = ModelTrainer().estimator_obj_filepath
        preprocessor_path = DataTransform().preprocessor_obj_file_path
        estimator_obj = load_object(estimator_path)
        preprocessor_obj = load_object(preprocessor_path)
        output = estimator_obj.predict(preprocessor_obj.transform(df))
        logging.info('Output has been returned')

        return output
    except Exception as e:
        raise CustomException(e,sys)
        
