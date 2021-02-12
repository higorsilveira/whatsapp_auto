#Import as bibliotecas
from os import truncate
from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from random import randint
import time
import pygame

#vars
contato = ['Higor Silveira']
mensagem = 'Reconheceu comando'

pygame.init()
game_is_running = True

#Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)

def main():
    buscar_contato(contato)
    time.sleep(3)
    global game_is_running
    while game_is_running:
        texto = ler_mensagem()
        if texto[:3] == '/d':
            print('reconheceu o comando')
            enviar_mensagem(mensagem)
        else:
            print('nao reconheceu comando')
        time.sleep(1)
        if str(texto).upper() == 'SAIR':
            game_is_running = False

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_pesquisa.click()
    time.sleep(1)
    campo_pesquisa.send_keys(contato)
    time.sleep(1)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    
    pos = str(mensagem).upper().find('D')
    pos_branco = str(mensagem[3:]).upper.find(' ')
    vezes = int(mensagem[3:pos])
    dado = int(mensagem[pos:pos_branco])
    plus = int(mensagem[pos_branco:])
    print('vezes = ',vezes)
    print('dado = ',dado)
    print('plus = ',plus)
    
    driver.quit()

    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(1)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(1)
    campo_mensagem[1].send_keys(Keys.ENTER)

def ler_mensagem():
    leitura = driver.find_elements_by_xpath("(//span[@class='_1VzZY selectable-text copyable-text']//span)[last()]")
    return leitura[0].text

def rolar_dado(vezes, dado, plus):
    result = 0 
    for i in range(vezes):
        result += randint(1,int(dado))
    result += plus
    return result

main()

