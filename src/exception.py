import sys

def errorMessageDetail(error, errorDetail:sys):
    _, _, exc_tb = errorDetail.exc_info()
    fileName = exc_tb.tb_frame.f_code.co_filename
    lineNumber = exc_tb.tb_lineno
    errorMessage = f'''Error occured in python file {fileName}, 
    line number {lineNumber}. Error Message: {str(error)}    
    '''

    return errorMessage

class customException(Exception):
    def __init__(self, errorMessage, errorDetail:sys):
        super().__init__(errorMessage)
        self.errorMessage = errorMessageDetail(errorMessage, errorDetail)

    def __str__(self):
        return self.errorMessage