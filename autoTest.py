from selenium import webdriver
from selenium.webdriver.common.by import By
from runTest import run_test
import pandas as pd

url = 'https://www.speedtest.net/pt'
headers = {
    'User-Agent': 'Mozilla/5.0 (<system-information>)\
     <platform> (<platform-details>) <extensions>'}

repeat = 2
load_repeat = 30
run_time = 45
load_pg = 2

ls_time = [load_pg, run_time, load_repeat]

dic_test_result = {'download': [], 'upload': []}

driver = webdriver.Chrome()

run_test(driver, repeat, ls_time, dic_test_result, url, By)

df = pd.DataFrame(dic_test_result)
df.to_csv('~/Downloads/teste_de_conexão.csv', encoding='utf-8', sep=';')
