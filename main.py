from deepface import DeepFace
import cv2
import os 

arquivos = os.listdir()
print(arquivos)
for arquivo in arquivos:
    if "jpg" in arquivo:
        #ler imagem
        imagem = cv2.imread(arquivo)
        #passar a imagem para a DeepFace
        resultado = DeepFace.analyze(imagem, actions=("age", "emotion"))
        #ver resultado 
        print(resultado)