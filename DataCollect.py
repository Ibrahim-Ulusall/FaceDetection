from Core.Utilities.ConfigurationTool.ProgramHelper import ProgramHelper
from Core.Utilities.ConfigurationTool.ConfigurationHelper import ConfigurationHelper
from Core.Utilities.Results.ErrorDataResult import ErrorDataResult
from Core.Utilities.Results.SuccessDataResult import SuccessDataResult
from Core.Utilities.Results.IDataResult import IDataResult
from Constans.Messages import Messages
import cv2
import os
import time

class DataCollection:
    _username : str = None
    _Directory = f"Datasets{ProgramHelper.Seperator()}Users"
    _newPath:str = None
    def __init__(self,username: str) -> None:
        self._username = username
        
    def UserExists(self) -> IDataResult:
        id,user = DataCollection.GetUser()
        newId:int = 0
        if len(id) > 0:
            self._newPath = self._username + '-' + str(id[-1] + 1)
        else:
            self._newPath = self._username + '-' + str(newId)
            print(self._newPath)
        path = os.path.join(self._Directory, self._newPath)
        result = ConfigurationHelper.PathExists(path)
        if not result.Success:
            return ErrorDataResult(result.Message)
        else:
            return SuccessDataResult(data=result)
        
    @staticmethod
    def Capture() -> IDataResult:
        try:
            camera = cv2.VideoCapture(0)
            frontal_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
            dataContext = {"camera" : camera,"FCascade":frontal_cascade,"PCascade":profile_cascade}

            return SuccessDataResult(data=dataContext)
        except Exception as e:
            raise ErrorDataResult(e.message)
        
    def FaceDetection(self):
        count = 1
        data = DataCollection.Capture().Data
        while True:
            ret, frame = data["camera"].read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frontal_faces = data["FCascade"].detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            profile_faces = data["PCascade"].detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for x, y, w, h in frontal_faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                name = self.name(count)
                cv2.imwrite(name,gray[y: y+h,x: x+w])
                count += 1
                print(name)
                
                if(count == 250):
                    ProgramHelper.ClearTerminal()
                    time.sleep(3)    
                    print("Şimdi Yüzünüzü Çevirin")

            for x, y, w, h in profile_faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                name = self.name(count)
                cv2.imwrite(name,gray[y: y+h,x: x+w])
                count += 1
                if(count >= 500):
                    ProgramHelper.ClearTerminal()
                    print("İşlem Tamamlandı")
            if count >= 500:
                time.sleep(2)
                ProgramHelper.ClearTerminal()
                break
            cv2.imshow("Frame", frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        data["camera"].release()
        cv2.destroyAllWindows()


    def program(self):
        result = self.UserExists()
        if not result.Success:
            return ErrorDataResult(result.Message)
        
        self.FaceDetection()
        return SuccessDataResult()    


    def name(self,count:int):
        name = os.path.join(self._Directory,self._newPath) + ProgramHelper.Seperator()  + f"{str(count)}.jpg"
        return name

    @staticmethod
    def GetUser():
        Ids = list()
        Users = list()
        
        for username in os.listdir(DataCollection._Directory):
            username:str = username.split('-')
            user:str = username[0]
            try:
                id:str = username[-1]        
                if id.isdigit():
                    Users.append(user)
                    Ids.append(int(id))
            except IndexError:
                Ids.append(0)
        return sorted(Ids),Users
