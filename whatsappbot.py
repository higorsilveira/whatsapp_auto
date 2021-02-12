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
contatos = ['O Vazio Entre Nós', 'Higor Silveira']

pygame.init()
game_is_running = True
time_wait = 0
time_think = 0
time_between = 0

#Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)

def main():
    global game_is_running
    while game_is_running:
        for contato in contatos:
            buscar_contato(contato)
            time.sleep(time_between)
            texto = ler_mensagem()
            if texto[:3] == '/d ':
                print('reconheceu o comando:', texto, texto[:2])
                enviar_mensagem(rolar_dado(texto))
            elif texto[:4] == '/tw ':
                config_tw(float(texto[3:]))
            elif texto[:4] == '/tt ':
                config_tt(float(texto[3:]))
            else:
                print('nao reconheceu comando', texto, texto[:2])
            if str(texto).upper() == '/SAIR':
                sair()

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_pesquisa.click()
    time.sleep(time_between)
    campo_pesquisa.send_keys(contato)
    time.sleep(time_between)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):

    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(time_wait)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(time_wait)
    campo_mensagem[1].send_keys(Keys.ENTER)

def ler_mensagem():
    leitura = driver.find_elements_by_xpath("(//span[@class='_1VzZY selectable-text copyable-text']//span)[last()]")
    return leitura[0].text

def rolar_dado(entrada):
    result = 0
    rolagem= 0

    pos = str(entrada).upper().rfind('D')
    pos_sinal = str(entrada[3:]).upper().find('+')
    if pos_sinal == -1:
        pos_sinal = str(entrada[3:]).upper().find('-')
    if pos_sinal == -1:
        pos_sinal = len(entrada)
    vezes = int(entrada[3:pos])
    dado = int(entrada[pos+1:pos_sinal+3])
    plus = int(0 if (entrada[pos_sinal+3:]) == '' else (entrada[pos_sinal+3:]))

    for i in range(vezes):
        rolagem += randint(1,int(dado))
    result = rolagem + plus

    out = '{}d{}+({}) -> {} + ({}) = {}'.format(vezes, dado, plus, rolagem, plus, result)

    return out

def sair():
    global game_is_running
    game_is_running = False

def welcome():
    mensagem = """Olá eu sou um Bot do Zap para rolagem de dados
    Posso ser utilizado com o comando /d xdysz
    ... onde x, y são números naturais e z um número inteiro
    ... onde s é um sinal entre duas opções + ou -
    Meu sistema utiliza faz uma verificação a cada 0.5 seg
    e no momento que um comando é passado eu paro 0.2 seg para pensar então, tenha paciência
    Logo terei implementações outros comandos."""

def config_tw(tw):
    global time_wait
    time_wait = tw

def config_tt(tt):
    global time_think
    time_think = tt

main()

