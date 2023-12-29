# Here, we'd be writing codes for the purpose of data cleaning, feature engineering and transforming features into a more usable form

import sys, os
from src.exception import CustomException
from src.logger import logging
from numpy import array
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from dataclasses import dataclass
from src.utils import save_object

@dataclass
class DataTransform:
    preprocessed_obj_file_path = os.path.join('artifacts','preprocessed.pkl')
    logging.info('Data transformation has begun')

    def initiate_transform(self, data_path):
        '''Accepts as input the data filepath. Performs imputation and transformation. Returns x and y as ndarray'''
        try:
            raw_df = pd.read_csv(data_path)
            self.x = raw_df.drop('math score', axis=1)
            self.y = raw_df['math score']
            logging.info('data has been read and splitted into x and y')

            num_features = self.x.select_dtypes(exclude="object").columns
            cat_features = self.x.select_dtypes(include="object").columns
            
            num_pipeline = Pipeline([('imputer', SimpleImputer(strategy='median')),
                                     ('scaler', StandardScaler())])
            cat_pipeline = Pipeline([('imputer', SimpleImputer(strategy='most_frequent')),
                                     ('one_hot_encoder', OneHotEncoder())])

            transformer_obj = ColumnTransformer([("encoded_cat", cat_pipeline, cat_features),
                                                 ("scaled_num", num_pipeline, num_features)], n_jobs=-1)
            x_transformed = transformer_obj.fit_transform(self.x)
            logging.info('Data features has been transformed successfully')

            save_object(file_path=self.preprocessed_obj_file_path, obj=transformer_obj)
            logging.info('pkl file has been saved successfully')

            return x_transformed, array(self.y), self.preprocessed_obj_file_path
        except Exception as e:
            logging.error(f'Error while transforming data: {e}')
            raise CustomException(e,sys)
        
