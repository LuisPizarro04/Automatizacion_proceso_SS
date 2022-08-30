from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from openpyxl import load_workbook
import time
import pandas as pd


#df = pd.read_excel('C:\Carpeta_compartida\Scripts&DB\Bases\Auto_reporte_Descarte\Auto_Descarte_25-08-2022.xlsx')
df = pd.read_excel('C:\Carpeta_compartida\Scripts&DB\Reportes\Automatizacion_descarte\Antigenos_Descartar20220829.xlsx')
# C:\Carpeta_compartida\Scripts&DB\Reportes\Automatizacion_descarte\Antigenos_Descartar20220829.xlsx
print(df)
