#Import as bibliotecas
from os import truncate
from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pygame



#cons
FRAMES_PER_SECOND = 25
SKIP_TICKS = 1000 / FRAMES_PER_SECOND

#vars
contato = ['Higor Silveira']
mensagem = 'Reconheceu comando'

pygame.init()
next_game_tick = pygame.time.get_ticks()
game_is_running = True
sleep_time = 0


#Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)

def main():
    buscar_contato(contato)
    time.sleep(5)
    global game_is_running, next_game_tick, sleep_time
    while game_is_running:
        print('entrou no loop')
        texto = ler_mensagem("(//span[@class='_1VzZY selectable-text copyable-text']//span)[last()]")
        if texto[:3] == '/d':
            enviar_mensagem(mensagem)
        else:
            print('nao reconheceu comando')
        
        next_game_tick += SKIP_TICKS
        sleep_time = next_game_tick - pygame.time.get_ticks()
        if sleep_time >= 0:
            time.sleep(sleep_time)
        else:
            print('estamos lentos')
        if texto == 'bot.quit':
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