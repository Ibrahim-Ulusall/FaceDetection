from DataCollect import DataCollection
from Core.Utilities.ConfigurationTool.ProgramHelper import ProgramHelper
from Constans.Messages import Messages
from Traning import Traning
from Models import TestModel
import time
import sys

class Program:
    
    def Run(self):
        print("""
            [ 0 ] : Add User
            [ 1 ] : Detection
            [ 3 ] : Quit

        """)
        try:
            choice = int(input('Choice -> '))
            if choice == 0:
                username = str(input("Username : "))
                if not username  or username.isspace():
                    print(Messages.UsernameCannotBeEmptyError)
                else:
                    dataCollection = DataCollection(username)
                    dataCollection.program()
                    print(dataCollection._Directory + ProgramHelper.Seperator() + dataCollection._newPath)
                    Traning.RecognizerAndSave(dataCollection._Directory + ProgramHelper.Seperator() + dataCollection._newPath)
                    model = TestModel()
                    model.Detection()
            elif choice == 1:
                model = TestModel()
                model.Detection()
            elif choice == 3:
                ProgramHelper.ClearTerminal()
                time.sleep(2)
                sys.exit()
            else:
                print(Messages.InvalidChoiceError)
        except Exception as e:
            print(e)

        

program = Program()
program.Run()