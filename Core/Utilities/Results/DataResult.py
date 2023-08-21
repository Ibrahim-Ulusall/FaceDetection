from .IDataResult import IDataResult
from .Result import Result

class DataResult(Result, IDataResult):
    def __init__(self, message:str, success:bool,data:object) -> None:
        self.Data = data
        super().__init__(message, success)