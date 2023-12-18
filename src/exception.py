import sys
from logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    # exec_tb holds info about the exceptions that has occured - the file and line no.
    file_name = exc_tb.tb_frame.f_code.co_filename
    err_mess = f'Error occured in python script name {file_name} line number {exc_tb.tb_lineno} error message {str(error)}'
    return err_mess

class CustomException(Exception):
    def __init__(self, err_mess, error_detail:sys):
        super().__init__(err_mess)
        self.err_mess = error_message_detail(err_mess, error_detail)

    def __str__(self):
        return self.err_mess
    