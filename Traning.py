import os 
import cv2
import numpy as np
from PIL.Image import open
from Core.Utilities.ConfigurationTool.ProgramHelper import ProgramHelper

class Traning:

    @staticmethod
    def getImages(path:str):
        ImagesPath = [os.path.join(path,image) for image in os.listdir(path)]
        Faces = list()
        Ids = list()
        for image in ImagesPath:
            FaceImage = open(image).convert('L')
            facesNumpyArray = np.array(FaceImage)
            Faces.append(facesNumpyArray)
            Ids.append(int(os.path.split(path)[-1].split('-')[-1]))
        return Faces,Ids
    
    @staticmethod
    def RecognizerAndSave(path:str):
        faces,id =  (Traning.getImages(path))
        recognizer = cv2.face.LBPHFaceRecognizer().create()
        recognizer.train(faces,np.array(id))
        recognizer.write('Trainer.yml')
        print('Completed!')

