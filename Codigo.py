# bibliotecas + pacote de códigos
# pip install pyautogui

import pyautogui
import time

pyautogui.click
pyautogui.write
pyautogui.press
pyautogui.hotkey
pyautogui.PAUSE = 0.5

# Passo a passo do seu programa 
# Passo 1: Entrar no sistema da empresa

# abriria o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press("enter")
# Fazer uma pausa maior pro site carregar 
time.sleep(3)


# Passo 2: Fazer login
# clicar no campo de email    


pyautogui.click(x=713, y=377)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")  #passar para o próximo campo
pyautogui.write("Bruxas2401?")
pyautogui.press("tab") #passar para o botão
pyautogui.press("enter")
# Fazer uma pausa maior pro site carregar 
time.sleep(3)


# Passo 3: Abrir a base da dados (importar o arquivo)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
        # Passo 4: Cadastrar 1 produto
        # codigo
        pyautogui.click(x=702, y=263) 
        codigo = str(tabela.loc[linha, "codigo"])
        pyautogui.write(codigo)
        pyautogui.press("tab") #passar para o proximo campo 

        # marca
        marca = str(tabela.loc[linha,"marca"])
        pyautogui.write(marca)
        pyautogui.press("tab")

        # tipo
        tipo = str(tabela.loc[linha,"tipo"])
        pyautogui.write(tipo)
        pyautogui.press("tab")

        # categoria
        categoria = str(tabela.loc[linha,"categoria"])
        pyautogui.write(categoria)
        pyautogui.press("tab")

        #preco unitario
        preco = str(tabela.loc[linha,"preco_unitario"])
        pyautogui.write(preco)
        pyautogui.press("tab")

        # custo
        custo = str(tabela.loc[linha,"custo"])
        pyautogui.write(custo)
        pyautogui.press("tab") 

        # obs
        obs= str(tabela.loc[linha,"obs"]) 
        [linha,"obs"]
        pyautogui.write(obs)
        pyautogui.press("tab")  # passar para o botaõ enviar 

        pyautogui.press("enter")
        # voltar pro inicio da tela 
        pyautogui.scroll(5000)




# Passo 5: Repetir o passo 4  até acabar a lista de produtos

