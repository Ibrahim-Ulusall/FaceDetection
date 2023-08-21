from .DataResult import DataResult

class SuccessDataResult(DataResult):
    def __init__(self, message: str = None, data: object = None) -> None:
        super().__init__(message, True, data)