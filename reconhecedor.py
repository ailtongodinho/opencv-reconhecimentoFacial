import cv2
from repository.FacesRepository import FacesRepository

def reconhecer(tipo = "E"):
    reconhecedor = None
    match tipo:
        case "E":
            detectorFace = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
            reconhecedor = cv2.face.EigenFaceRecognizer_create()
            reconhecedor.read("classificadorEigen.yml")
        case "F":
            detectorFace = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
            reconhecedor = cv2.face.FisherFaceRecognizer_create()
            reconhecedor.read("classificadorFisher.yml")
        case "L":
            detectorFace = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
            reconhecedor = cv2.face.LBPHFaceRecognizer_create()
            reconhecedor.read("classificadorLBPH.yml")
        case _:
            raise Exception("Tipo de Reconhecedor não identificado")

    largura, altura = 220, 220
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    camera = cv2.VideoCapture(0)
    fr = FacesRepository()
    fr.GetConnection()

    try:
        while (True):
            conectado, imagem = camera.read()
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            facesDetectadas = detectorFace.detectMultiScale(imagemCinza,
                                                            scaleFactor=1.5,
                                                            minSize=(30,30))
            for (x, y, l, a) in facesDetectadas:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
                cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
                id, confianca = reconhecedor.predict(imagemFace)
                nome = fr.QueryUser(id)[1]
                cv2.putText(imagem, nome, (x, y + a + 30), font, 2, (0, 0, 255))
                cv2.putText(imagem, str(confianca), (x,y + (a+50)), font, 1, (0,0,255))

            cv2.imshow("Face", imagem)
            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()
        fr.CloseConnection()
