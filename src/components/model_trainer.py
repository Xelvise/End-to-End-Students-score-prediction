# Here, we'd be writing codes for the purpose of training the model

import os, sys
from numpy import linspace
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor

from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model
from sklearn.model_selection import train_test_split as tts

@dataclass
class ModelTrainer:
    trained_model_filepath = os.path.join('artifacts','model.pkl')

    def initiate_model_training(self,x,y,preprocessed_path=None):
        '''Accepts independent and target variables (x and y). Splits x and y into train and test set.\n
        Fits a couple of Regressor estimators to the training set.\n
        Performs Hyperparameter tuning and returns the score of the best performant of them all (based on the test set)'''
        try:
            logging.info('splitting train and test input data')
            x_train,x_test,y_train,y_test = tts(x,y,test_size=0.25,random_state=0)

            models = {
            "Linear Regression": LinearRegression(),
            "K-Neighbors Regressor": KNeighborsRegressor(),
            "Decision Tree": DecisionTreeRegressor(),
            "Random Forest Regressor": RandomForestRegressor(),
            "XGBRegressor": XGBRegressor(),
            "AdaBoost Regressor": AdaBoostRegressor(),
            "Gradient Boosting": GradientBoostingRegressor()}

            params = {
                'Linear Regression': {k:[v] for k,v in LinearRegression().get_params().items()},
                'Decision Tree': {'ccp_alpha':[round(i,3) for i in linspace(0,0.02,11)]},
                'Random Forest Regressor': {'ccp_alpha':[round(i,3) for i in linspace(0,0.02,11)],
                                            'n_estimators': linspace(0,256,11, dtype=int)},
                'XGBRegressor': {'learning_rate':[.1,.01,.05,.001],
                                 'n_estimators':linspace(8,256,11, dtype=int)},
                'AdaBoost Regressor': {'learning_rate':[.1,.01,.05,.001],
                                       'n_estimators':linspace(8,256,11, dtype=int)},
                'K-Neighbors Regressor': {'n_neighbors':[5,7,9,11]},
                'Gradient Boosting': {'learning_rate':[.1,.01,.05,.001],
                                      'n_estimators':linspace(8,256,11, dtype=int)}                  
            }

            model_report = evaluate_model(x_train,x_test,y_train,y_test,models,params)
            best_model_score = max(model_report.values())
            best_model_name = ''
            for k,v in list(model_report.items()):
                if v == best_model_score:
                    best_model_name += k

            if best_model_score<0.6:
                raise CustomException('No best model found')
            logging.info(f'Found best model for both train and test set - {best_model_name}')

            best_model = models[best_model_name]  # returns an untrained estimator of the best model
            model_obj = best_model.fit(x_train,y_train)  # returns a fitted estimator  
            save_object(self.trained_model_filepath, model_obj)

            return best_model_score  # returns performance of the best estimator
        
        except Exception as e:
            raise CustomException(e,sys)