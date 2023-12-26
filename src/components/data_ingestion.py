# Here, we'd be writing modular codes for the purpose of reading or ingesting the dataset

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    '''Holds 3 attributes that are assigned the paths of the train, test and raw data, respectively.'''
    train_data_path: str = os.path.join('artifacts', 'train.csv') # creates a path, taking 'artifacts' as the root dir, and 'train.csv' as the file
    test_data_path: str = os.path.join('artifacts', 'test.csv') # creates a path, taking 'artifacts' as the root dir, and 'test.csv' as the file
    raw_data_path: str = os.path.join('artifacts', 'data.csv') # creates a path, taking 'artifacts' as the root dir, and 'data.csv' as the file

@dataclass
class DataIngestion:
    '''
    'ingestion_config' is set as an instance of the DataIngestionConfig class.
    This is done so that we can access the attributes of the DataIngestionConfig class.
    The initiate_data_ingestion method is used to read the dataset, split it into train and test sets,
    and save the train and test sets as csv files in the artifacts folder.
    '''

    ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')
        try:
            df = pd.read_csv('notebook/StudentsPerformance.csv')
            logging.info('Data read successfully')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) 
            # os.makedirs creates a directory, with respect to the dir_name (...artifacts/train.csv), so long as it doesn't exist
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            # having read the dataset, it is then stored as 'data.csv' inside the already created dir (i.e, artifacts/data.csv)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            # next, df is splitted into train and test sets, with the test set being 20% of the entire dataset
             
            logging.info('Train test split initiated')

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            # the train_set is stored as 'train.csv' inside the already created dir (i.e, artifacts/train.csv)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            # the test_set is stored as 'test.csv' inside the already created dir (i.e, artifacts/test.csv)
            logging.info('Data ingestion completed')

            return (
                self.ingestion_config.train_data_path, # returns the path to the train set
                self.ingestion_config.test_data_path  # returns the path to the test set
            )
        except Exception as e:  # e denotes the string representation of the error
            logging.error(f'Error while ingesting data: {e}')
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    DataIngestion().initiate_data_ingestion()