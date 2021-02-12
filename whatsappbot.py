#Import as bibliotecas
from os import truncate
from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
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
        print('entrou no loop')
        texto = ler_mensagem("(//span[@class='_1VzZY selectable-text copyable-text']//span)[last()]")
        print('digitado', texto)
        if texto[:3] == '/d':
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
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(1)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(1)
    campo_mensagem[1].send_keys(Keys.ENTER)

def ler_mensagem(local):
    leitura = driver.find_elements_by_xpath(local)
    
    return leitura

main()