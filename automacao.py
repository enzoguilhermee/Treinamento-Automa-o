# Passo a passo do projeto

#__________________________________________________________________
# Passo 1: Entrar no sistema da empresa 
#__________________________________________________________________

    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui as py
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
py.PAUSE = 0.3

# abrir o navegador (chrome)
py.press("win")
py.write("Opera")
py.press("enter")
time.sleep(2)

# entrar no link 
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")
time.sleep(3)

#__________________________________________________________________
# Passo 2: Fazer login
#__________________________________________________________________

# selecionar o campo de email
py.click(x=670, y=406)
# escrever o seu email
py.write("pythonimpressionador@gmail.com")
py.press("tab") # passando pro próximo campo
py.write("sua senha")
py.press("enter") # enter para confirmar a senha e login e entrar no sistema
time.sleep(3)

#__________________________________________________________________
# Passo 3: Importar a base de produtos pra cadastrar
#__________________________________________________________________

import pandas as pd

tabela_produtos = pd.read_csv("produtos.csv") # vai abrir a tabela através da biblioteca pandas

print(tabela_produtos)


#__________________________________________________________________
# Passo 4: Cadastrar um produto
#__________________________________________________________________

for linha in tabela_produtos.index:
    # clicar no campo de código
    py.click(x=677, y=292)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela_produtos.loc[linha, "codigo"]
    time.sleep(1)
    # preencher o campo
    py.write(str(codigo))
    py.press("tab")
    # preencher o campo
    py.write(str(tabela_produtos.loc[linha, "marca"]))
    py.press("tab")
    py.write(str(tabela_produtos.loc[linha, "tipo"]))
    py.press("tab")
    py.write(str(tabela_produtos.loc[linha, "categoria"]))
    py.press("tab")
    py.write(str(tabela_produtos.loc[linha, "preco_unitario"]))
    py.press("tab")
    py.write(str(tabela_produtos.loc[linha, "custo"]))
    py.press("tab")
    obs = tabela_produtos.loc[linha, "obs"]
    if not pd.isna(obs):
        py.write(str(tabela_produtos.loc[linha, "obs"]))
    py.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    py.scroll(5000)

    #__________________________________________________________________
    # Passo 5: Repetir o processo de cadastro até o fim
    #__________________________________________________________________'''
