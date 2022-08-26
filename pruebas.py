from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from openpyxl import load_workbook
import time
import pandas as pd
from datetime import datetime

from selenium.webdriver.remote.webelement import WebElement

# Driver para ingresar a la página inicial de EPI
# driver = webdriver.Chrome(executable_path=r"C:\Users\luis.pizarro.a\PycharmProjects\Auto_Descarte_Eno\chromedriver.exe")
# driver.get("https://epivigila.minsal.cl/index.php/administracion/ver-formulario/50")
# time.sleep(3)  # tiempo de carga

df = pd.read_excel('C:\Carpeta_compartida\Scripts&DB\Bases\Auto_reporte_Descarte\Auto_Descarte_25-08-2022.xlsx')
print(df)



"""
# Bloque para agregar desconocido en la previsión listo.
prevision = driver.find_element(By.XPATH, "//*[@id='select2-id_prevision_laboral-container']")
prevision.click()
time.sleep(3)
mov_lis = driver.find_element(By.XPATH,"//*[@id='select2-id_prevision_laboral-results']")
mov_lis.find_element(By.XPATH, "//*[@id='select2-id_prevision_laboral-results']/li[7]").click()"""


