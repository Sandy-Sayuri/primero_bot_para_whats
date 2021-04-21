#simula o uso do navegador atraves de automação web
from selenium import webdriver
#permita aguradar alguns segundos para escaniar a tela do seu pc usando o cel
import time
#simaula o uso no navegador sem ter que baixar ferramentas add
from webdriver_manager.chrome import ChromeDriverManager
#pega a funcionalidade do teclado
from selenium.webdriver.common.keys import Keys 
#--------------Navegar até o whatapp web----------
#definido configuração do web drive
drive= webdriver.Chrome(ChromeDriverManager().install())
#aqui coloca o link do app
drive.get("https://web.whatsapp.com/")
#espera 30 segundos
time.sleep(10)
#------------------Definir contatos e grupos e a mensagem a ser enviada-------------------
#contados escolhidos
contatos=["Acontece","ヴにしおー"]
#mensagem escolhida
mensagem='teste iguinore a mensagem '
#----------------buscar contatos/grupo---------------
def  buscar_contato(contato):
    #aqui escolhe em que clicar
    campo_pesquisa=drive.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
   
    #clique no  lugar indicado
    campo_pesquisa.click()
    #digita o nome da pessoa
    campo_pesquisa.send_keys(contato)
    #para apertar enter
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    #aqui escolhe em que clicar
    campo_mensagem=drive.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    #escolhe só o campo de baixo
    campo_mensagem[1].click()
    #escolhe a mensagem
    campo_mensagem[1].send_keys(mensagem)
    #envia e mensagem
    campo_mensagem[1].send_keys(Keys.ENTER)





for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
#----------------Campo de pesquisa 'copyable-text selectable-text'-------------------------------------
#----------------Campo de mensagem privada "copyable-text selectable-text"-------------------------------------------------