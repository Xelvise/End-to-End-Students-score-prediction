# Here, we'd define the basic utilities/functions needed by other modules in this project, where it can be called and used

import pickle, sys, os
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import RandomizedSearchCV

def save_object(file_path, obj):
    '''Saves the given object (probably, an estimator) into the given file path'''
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        # os.makedirs creates an empty directory, with respect to the given dir_name, so long as it doesn't exist

        with open(file_path,'wb') as f:  # f is used to reference the filepath, after opening the file
            pickle.dump(obj, f)  # the transformer obj is stored in the filepath

    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    '''Returns object that is present in the given file path'''
    try:
        with open(file_path,'rb') as f:
            return pickle.load(f)
        
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(x_train,x_test,y_train,y_test,models:dict,params:dict):
    '''Returns as a dict all estimators with thier corresponding test_pred_score'''
    try:
        report = dict()

        for i in range(len(models)):
            model = list(models.values())[i]  # list of estimators being indexed
            param = params[list(models.keys())[i]]  # list of params being indexed, belonging to each estimator

            rs = RandomizedSearchCV(model,param,cv=3).fit(x_train,y_train)
            model.set_params(**rs.best_params_)  # sets the params of the indexed estimator to that which is selected by RandomizedSearch
            model.fit(x_train,y_train)

            y_train_pred = model.predict(x_train)  # prediction based off training data
            y_test_pred = model.predict(x_test)  # prediction based off test data
            train_pred_score = r2_score(y_train,y_train_pred)
            test_pred_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_pred_score
        return report  # returns report consisting of estimator names and thier corresponding test_pred_score
    
    except Exception as e:
        raise CustomException(e,sys)
