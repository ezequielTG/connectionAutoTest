from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from tkinter import *
from createComponents import build_label
from createComponents import build_entry
from runTest import run_test
import pandas as pd
import math

url = 'https://www.speedtest.net/pt'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome / 119.0.0.0 Safari / 537.36'}

# -- Não está em uso no momento --
# Motivo: ao passar options para webdriver.ChromeOptions,
#        ocorre um erro que identifica a passagem de um
#        argumento além do permitido
options = webdriver.ChromeOptions()
options.add_argument('--headless')
#

repeat = 0
load_repeat = 0
run_time = 0
load_pg = 0


def define_param_run():
    global repeat, load_repeat, run_time, load_pg

    repeat = int(def_repeat.get())
    load_repeat = int(def_load.get())
    run_time = int(def_run_time.get())
    load_pg = int(def_interval.get())

    print(repeat, load_repeat, run_time, load_pg)


colLab = 0
colEnt = 1

window = Tk()
window.geometry("570x296")
window.title("Configurar Teste")

info = Label(window, text="Defina os parâmetros de execução do teste:")
info.grid(column=0, row=0)

label_repeat = build_label(colLab, 2, window, "Repetições: ")
def_repeat = build_entry(colEnt, 2, window)

label_load = build_label(colLab, 3, window, "Carregamento: ")
def_load = build_entry(colEnt, 3, window)

label_run = build_label(colLab, 4, window, "Duração: ")
def_run_time = build_entry(colEnt, 4, window)

label_interval = build_label(colLab, 5, window, "Intervalo: ")
def_interval = build_entry(colEnt, 5, window)

btn_apply = Button(window, text="Aplicar", command=define_param_run, width=6, height=1)
btn_apply.grid(column=2, row=6, padx=10, pady=10)

btn_close = Button(window, text="Fechar", command=window.destroy, width=6, height=1)
btn_close.grid(column=1, row=6, padx=10, pady=10)

window.mainloop()

ls_time = [load_pg, run_time, load_repeat]

dic_test_result = {'download': [], 'upload': []}

driver = webdriver.Chrome()

run_test(driver, repeat, ls_time, dic_test_result, url, By)

# Resolver o cálculo da média das velocidades de download e upload

list_values = dic_test_result.values()
print(list_values)

average = 0

df = pd.DataFrame(dic_test_result)
df.to_csv('~/Downloads/teste_de_conexão.csv', encoding='utf-8', sep=';')
