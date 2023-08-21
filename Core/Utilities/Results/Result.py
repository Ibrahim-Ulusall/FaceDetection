from .IResult import IResult

class Result(IResult):
    def __init__(self, message:str, success:bool) -> None:
        self.Message = message
        self.Success = success