import os

class ProgramHelper:

    @staticmethod
    def ClearTerminal():
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
        else:
            pass
    def Seperator():
        return os.sep
