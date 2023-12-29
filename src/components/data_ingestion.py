# Here, we'd be writing modular codes for the purpose of reading or ingesting the dataset

import os, sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
from src.components.data_preprocessing import DataTransform
from src.components.model_trainer import ModelTrainer
import warnings; warnings.filterwarnings('ignore')

@dataclass
class DataIngestionConfig:
    '''Holds 3 attributes that are assigned the paths of the train, test and raw data, respectively.'''
    train_data_path: str = os.path.join('artifacts', 'train.csv') # creates a path, taking 'artifacts' as the root dir, and 'train.csv' as the file
    test_data_path: str = os.path.join('artifacts', 'test.csv') # creates a path, taking 'artifacts' as the root dir, and 'test.csv' as the file
    raw_data_path: str = os.path.join('artifacts', 'data.csv') # creates a path, taking 'artifacts' as the root dir, and 'data.csv' as the file

@dataclass
class DataIngestion:
    '''
    The initiate_data_ingestion method is used to read the dataset, split it into train and test sets,
    and save the train and test sets as csv files in the artifacts folder.
    '''
    train_data_path = DataIngestionConfig().train_data_path
    test_data_path = DataIngestionConfig().test_data_path
    raw_data_path = DataIngestionConfig().raw_data_path

    def initiate_data_ingestion(self):
        '''Returns the data path of the already ingested dataset'''
        logging.info('Entered the data ingestion method or component')
        try:
            df = pd.read_csv('notebook/StudentsPerformance.csv')
            logging.info('Data read successfully')

            os.makedirs(os.path.dirname(self.train_data_path), exist_ok=True) 
            # os.makedirs creates an empty directory, with respect to the dir_name (artifacts/train.csv), so long as it doesn't exist
            
            df.to_csv(self.raw_data_path, index=False, header=True)
            # having read the dataset, it is then stored as 'data.csv' inside the already created dir (i.e, artifacts/data.csv)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            # next, df is splitted into train and test sets, with the test set being 20% of the entire dataset
             
            logging.info('Train-test split initiated')

            train_set.to_csv(self.train_data_path, index=False, header=True)
            # the train_set is stored as 'train.csv' inside the already created dir (i.e, artifacts/train.csv)
            test_set.to_csv(self.test_data_path, index=False, header=True)
            # the test_set is stored as 'test.csv' inside the already created dir (i.e, artifacts/test.csv)
            logging.info('Data ingestion completed')

            return self.raw_data_path  # returns the path to the raw data set
        except Exception as e:  # e denotes the string representation of the error
            logging.error(f'Error while ingesting data: {e}')
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    data = DataIngestion().initiate_data_ingestion()
    x, y, _ = DataTransform().initiate_transform(data)  # preprocessed path isn't needed
    print(ModelTrainer().initiate_model_training(x,y))