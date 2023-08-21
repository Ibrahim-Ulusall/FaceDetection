import os
from Core.Utilities.Results.SuccessDataResult import SuccessDataResult
from Core.Utilities.Results.ErrorDataResult import ErrorDataResult
from Core.Constans.Messages import Messages

class ConfigurationHelper:
    @staticmethod
    def PathExists(path: str):
        if not os.path.exists(path=path):
            os.makedirs(path)
            return SuccessDataResult()
        return ErrorDataResult(Messages.FolderAlreadyExistsError)
        