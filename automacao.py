import time
import pandas
import pyautogui
import pyperclip
import pandas as pd
pyautogui.PAUSE = 2

#entrar no sistema
pyautogui.press("win")
pyautogui.click(x=398, y=220, clicks= 1)
time.sleep(3)


#navegar no sistema
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")
time.sleep(3)
#encontarr base de dados
pyautogui.click(x=430, y=339, clicks= 2)

#baixar base de dados
pyautogui.click(x=460, y=413, clicks= 1)
pyautogui.click(x=1131, y=183, clicks= 1)
pyautogui.click(x=878, y=644, clicks= 1)

#calcular indicadores
tabela= pandas.read_excel(R"C:\Users\gabir\Downloads\Vendas - Dez.xlsx")
quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()
print(quantidade)
print(faturamento)

#entar no email
pyautogui.press("win")
pyautogui.write("edge")
time.sleep(3)
pyautogui.press("enter")
time.sleep(3)
pyperclip.copy("https://outlook.live.com/mail/0/")
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")
time.sleep(3)

#mandar email
pyautogui.click(x=215, y=177, clicks= 1)
time.sleep(3)
pyautogui.write("gabi.rod.braga@hotmail.com")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("tab")

#corpo email
texto = f""" 
Prezados, Bom dia !

O faturamento de ontem foi de = R$ {faturamento:,.2f}
A quantidade de peças vendidas = {quantidade:,}

att 
Gabi Braga
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl" , "v")

#enviar o

pyautogui.hotkey("ctrl" , "enter")
