import dill, sys, os
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        # os.makedirs creates an empty directory, with respect to the dir_name (artifacts/preprocessed.pkl), so long as it doesn't exist

        with open(file_path,'wb') as f:  # f is used to reference the file path
            dill.dump(obj, f)  # the transformer obj is stored in the file_path

    except Exception as e:
        raise CustomException(e, sys)