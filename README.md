ProjPerspectiva
===============

Aplicação que faz uma Projeção Perspectiva usando a biblioteca GUI Tkinter do Python.

Execução
--------

Para rodar o programa é necessário o Python 2.7 ou superior. O arquivo que deverá ser executado é o *main.py*. Para executar em linha de comando, vá até a pasta onde o arquivo está e digite:
    
    python main.py

Uso
---

A interface possui um botão Escolher Objeto onde é possivel escolher um arquivo de entrada com as coordenadas de um objeto. Os arquivos padrões estão na pasta ./testes desse projeto.

O arquivo padrão do prisma seria:

    0 0 0
    2 0 0
    2 3 0
    0 3 0
    1 2 1
    1 1 1
    #
    0 1 5
    1 2 4 5
    2 3 4
    0 5 4 3
    0 3 2 1


onde os valores antes do # são as coordenadas dos pontos separadas por espaços, os pontos são separados por linhas e recebem números automaticamente começando de 0. Já os valores abaixo do # são os pontos das superficies separados por espaços, as superficies são separadas por linhas.
