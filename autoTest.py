from selenium import webdriver
from selenium.webdriver.common.by import By
from runTest import run_test
import pandas as pd


#Endereço do site e as informações para que o servidor identifique 
#quem está enviando a requisição 

url = 'https://www.speedtest.net/pt'
headers = {
    'User-Agent': 'Mozilla/5.0 (<system-information>)\
     <platform> (<platform-details>) <extensions>'}

#repeat -> Número de vezes que o teste será realizado
#runt_ime -> O tempo estimado para a execução do teste
#load_repeat -> Intervalo para o próximo teste
#load_pg -> Tempo estimado para carregamento de página completo

repeat = 2
load_repeat = 30
run_time = 45
load_pg = 2

ls_time = [load_pg, run_time, load_repeat]

dic_test_result = {'download': [], 'upload': []}

driver = webdriver.Chrome()

run_test(driver, repeat, ls_time, dic_test_result, url, By)

#gera a tabela, converte para .csv e salva em downloads

df = pd.DataFrame(dic_test_result)
df.to_csv('~/Downloads/teste_de_conexão.csv', encoding='utf-8', sep=';')
