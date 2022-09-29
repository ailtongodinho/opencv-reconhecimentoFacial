# Reconhecimento Facial utilizando a biblioteca OpenCV

O projeto tem o objetivo de executar o reconhecimento facial dos usuários utilizando os componentes EigenFaces, FisherFaces e LPBH Faces da biblioteca OpenCV. 
Também é utilizado o banco de dados SQLite para gravar dados do usuário.

## Interface do usuário

Para facilitar o dóminio do Software, foi criada a interface do usuário (aqui não se trata de uma interface leiga, e sim, para facilitar o acesso as ferramentas).

Na interface, é possível cadastrar um novo usuário, Treinar os modelos disponíveis e Reconhecer o usuário

```
============================================================
-1 - Zerar banco de dados e imagens
 0 - Sair
 1 - Incluir novo usuário
 2 - Treinar modelo
 3 - Reconhecer usuário
============================================================
```

## Banco de dados

A biblioteca SQLite foi escolhida para fornecer um banco de dados simples, rápido e útil, diretamente do armazenamento do computador. 

O objetivo é salvar o nome do usuário e atribí-lo um ID.

## Links úteis

- https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html
- https://docs.python.org/3/library/sqlite3.html
