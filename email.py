import pyautogui
import time
import pyperclip
#abrindo email
pyautogui.press("win")
pyautogui.write("edge")
time.sleep(3)
pyautogui.press("enter")
time.sleep(3)
pyperclip.copy("https://outlook.live.com/mail/0/")
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")
time.sleep(3)

#enviando email
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

#enviar o email
pyautogui.hotkey("ctrl" , "enter")