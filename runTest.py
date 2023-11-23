#A função run_test recebe como parâmetros o navegador(driver),
#número de repetições do teste(num_test), uma lista com os 
#tempos extimados para execução do código(ls_time), o dicionário
#que guardará os resultados de download e upload(dic), endereço do
#site(url) e o by(By).
#
#Ela acessa o site, encotra o botão e executa o teste. Por fim,
#após o término da execução do teste, captura os resultados e
#adiciona ao dicionário.


from bs4 import BeautifulSoup
import time


def run_test(driver, num_test, ls_time, dic, url, by):
    for i in range(1, num_test + 1):
        i_time = 0
        driver.get(url)

        time.sleep(ls_time[i_time])

        i_time += 1

        driver.find_element(by.CLASS_NAME, 'js-start-test').click()
        time.sleep(ls_time[i_time])

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        download_vlc = soup.find('span', class_='download-speed').get_text().strip()
        upload_vlc = soup.find('span', class_='upload-speed').get_text().strip()

        dic['download'].append(download_vlc)
        dic['upload'].append(upload_vlc)

        i_time += 1
        time.sleep(ls_time[i_time])
