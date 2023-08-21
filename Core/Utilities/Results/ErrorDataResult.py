from .DataResult import DataResult

class ErrorDataResult(DataResult):
    def __init__(self, message: str = None, data: object = None) -> None:
        super().__init__(message, False, data)