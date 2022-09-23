import os
from math import fabs
from captura import capturar
from reconhecedor import reconhecer
from repository.FacesRepository import FacesRepository
from treinamento import treinar

# Menu Princial
def carregarMenuPrincipal():
    print("============================================================")
    print("-1 - Zerar banco de dados e imagens")
    print(" 0 - Sair")
    print(" 1 - Incluir novo usuário")
    print(" 2 - Treinar modelo")
    print(" 3 - Reconhecer usuário")
    print("============================================================")
    return int(input("Selecione uma das opções acima: "))

while True:
    menu = carregarMenuPrincipal()
    try:
        match menu:
            case 0:
                exit()
            case 1:
                capturar(30)
            case 2:
                treinar("T")
            case 3:
                reconhecer()
            case -1:
                escolhaZerar = input("Tem certeza que deseja zerar o banco de dados e as imagens? (S/N):").upper()
                if escolhaZerar == "S":
                    FacesRepository.ResetDatabase()
                    for caminhoImagem in [os.path.join('fotos', f) for f in os.listdir('fotos')]:
                        os.remove(caminhoImagem)
    except Exception as ex:
        print(f"Ocorreu um erro durante a solicitação: {ex}")