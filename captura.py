from datetime import datetime
from random import Random
from time import sleep
from tkinter import E
import cv2
import numpy as np
from repository.FacesRepository import FacesRepository

def capturar(numeroAmostras = 25):
    classificador = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
    classificadorOlho = cv2.CascadeClassifier("haarcascade-eye.xml")
    camera = cv2.VideoCapture(0)
    amostra = 1
    #   Consulta ultimo ID
    nome = input('Digite seu nome completo: ').capitalize()
    fr = FacesRepository()
    fr.GetConnection()
    usuario = fr.GetUser(nome)
    
    if usuario is not None:
        sobrescrever = input(f"Usuário {nome} já existe! Deseja sobrescrever a captura? (S/N): ").upper()
        if sobrescrever != "S":
            return 

    if usuario is not None:
        id = id = usuario[0]
    else:
        id = fr.NewUser(nome)

    largura, altura = 220, 220
    print("Capturando as faces...")
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    dataCaptura = datetime.now()
    try:
        while True:
            seconds = 0
            waitSeconds = 2.5

            conectado, imagem = camera.read()
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            #print(np.average(imagemCinza))
            facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                            scaleFactor=1.5,
                                                            minSize=(150,150))
            cv2.putText(imagem, f"Amostra {amostra} de {numeroAmostras}", (0, 30), font, 2, (0, 0, 255))
            for (x, y, l, a) in facesDetectadas:
                cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
                mediaImagem = int(np.average(imagemCinza))
                cv2.putText(imagem, f"{mediaImagem}%", (x, y + a + 30), font, 2, (0, 0, 255))
                regiao = imagem[y:y + a, x:x + l]
                regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
                olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)
                for (ox, oy, ol, oa) in olhosDetectados:
                    cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)
                    #if cv2.waitKey(1) & 0xFF == ord('q'):
                    # espera x segundos para interface do usuário
                    seconds = (datetime.now() - dataCaptura).total_seconds()
                    if  mediaImagem > 90 and seconds > waitSeconds:
                        dataCaptura = datetime.now()
                        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                        cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg", imagemFace)
                        print("Foto " + str(amostra) + " capturada com sucesso!")
                        amostra += 1

            cv2.imshow("Face", imagem)
            cv2.waitKey(1)
            if (amostra >= numeroAmostras + 1):
                break

        print("Faces capturadas com sucesso!")
        print("Usuário criado com sucesso!")
    finally:
        camera.release()
        cv2.destroyAllWindows()
        fr.CloseConnection()
