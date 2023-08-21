import cv2
from DataCollect import DataCollection

class TestModel:

    def GetUser(self):
        nameList = {}

        data = DataCollection.GetUser()

        for i in range(len(data[0])):
            nameList[data[0][i]] = data[1][i]
        print(nameList)                 
        return nameList

    def Detection(self):

        camera = cv2.VideoCapture(0)
        faceClassifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        recognizer = cv2.face.LBPHFaceRecognizer().create()
        while True:
            ret,frame = camera.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            
            recognizer.read('Trainer.yml')
            
            detect = faceClassifier.detectMultiScale(gray,1.3,5)

            for x,y,w,h in detect:
                serial , confidence = recognizer.predict(gray[y:y+h,x:x+w])
                print(f'Serial Id : {serial} Confidence : {confidence}')
                
                if confidence < 50:
                    cv2.putText(frame,self.GetUser()[serial],(x,y-40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                else:
                    cv2.putText(frame,'Unkown',(x,y-40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow("Face Detection",frame)
            key = cv2.waitKey(1)
            if(key == ord('q')):
                break

        camera.release()
        cv2.destroyAllWindows()
