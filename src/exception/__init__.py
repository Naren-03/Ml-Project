import os,sys

class CustomException(Exception):
    def __init__(self,error_message:Exception, error_details:sys) : #type:ignore
        self.error_message = CustomException.get_detailed_error_message(error_message=error_message,error_details=error_details)
    
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_details:sys)->str: # type:ignore
        _, _, exce_tb = error_details.exc_info()
        
        exception_block_line_number = exce_tb.tb_frame.f_lineno #type:ignore
        try_block_line_number = exce_tb.tb_lineno #type:ignore
        file_name = exce_tb.tb_frame.f_code.co_filename #type:ignore

        error_message = f"""Error occurred in execution of :
        [{file_name}] at 
        try block line number : [{try_block_line_number}]
        and exception block line number : [{exception_block_line_number}]
        error message: [{error_message}] """ # type: ignore

        return error_message # type: ignore
    
    def __str__(self) :
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str() #type:ignore