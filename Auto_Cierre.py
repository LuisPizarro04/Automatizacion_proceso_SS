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
driver = webdriver.Chrome(executable_path=r"C:\Users\luis.pizarro.a\PycharmProjects\Auto_Descarte_Eno\chromedriver.exe")
driver.get("https://epivigila.minsal.cl/index.php/administracion/ver-formulario/50")
time.sleep(3)  # tiempo de carga

# df = pd.read_excel('C:\Carpeta_compartida\Scripts&DB\Bases\Auto_reporte_Descarte\Auto_Descarte_25-08-2022.xlsx')
df = pd.read_excel('C:\Carpeta_compartida\Scripts&DB\Reportes\Automatizacion_descarte\Antigenos_Descartar20220829.xlsx')
# C:\Carpeta_compartida\Scripts&DB\Reportes\Automatizacion_descarte\Antigenos_Descartar20220829.xlsx
print(df)

# LOGIN EN EPIVIGILA CON USER Y PASS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print("Ingresando Usuario.......")
usuario = driver.find_element(By.NAME, "rut_usuario")
usuario.send_keys("192572843")
print("Usuario ingresado exitosamente")
print("Ingresando Contraseña.......")
contrasena = driver.find_element(By.NAME, "password")
contrasena.send_keys("Minsal2021")
print("Contraseña ingresada exitosamente")
print("Iniciando sesión.......")
loginbutton = driver.find_element(By.XPATH, "//input[@type='submit'][@type='submit']")
loginbutton.click()
time.sleep(5)
print("Esperando captcha.......")
time.sleep(5)
print("Ingresando a la notificación....")
time.sleep(5)

for i in range(len(df)):
    # Modificación de la fecha
    f_p_c = str(df.iloc[i]['fecha_toma_muestra'])
    dia = f_p_c[8:10]
    mes = f_p_c[5:7]
    agno = f_p_c[0:4]
    fecha_p_c = dia + "-" + mes + "-" + agno
    # ENTRAR A LA NOTIFICACIÓN POR UN FOLIO /50/FOLIO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    notificacion = "https://epivigila.minsal.cl/index.php/administracion/ver-formulario/50/"
    folio = df.iloc[i]['numero_folio']
    folio = folio + 50000
    enlacenotificacion = notificacion + str(folio)
    print("Ingresando a la sección 1 del registro: ", i)
    # SECCIÓN 1 IDENTIFICACIÓN DEL CASO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -Ir a la sección Identificación del caso----------------------------------------------------------------------
    driver.get(enlacenotificacion)
    time.sleep(4)
    # SE DEBE INGRESAR DESCONOCIDO EN OCUPACIÓN PRINCIPAL  Y RUBRO: SI ESTOS ESTÁN VACIOS
    ocupacion_principal = driver.find_element(By.XPATH, "//*[@id='actividad_laboral_declarada']")
    ocupacion_principal.send_keys("DESCONOCIDO")
    rubro = driver.find_element(By.XPATH, "//*[@id='rubro_trabajo']")
    rubro.send_keys("DESCONOCIDO")
    # SECCIÓN 2 ANTECEDENTES CLINICOS Y EPIDEMIOLOGICOS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -Ir a la sección Antecedentes clínicos y epidemiológicos------------------------------------------------------
    print("Ingresando a la sección 2del registro: ", i)
    seccion_2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Antecedentes clínicos y epidemiológicos')
    seccion_2.click()
    time.sleep(3)
    # Ingreso de la fecha de primera consulta
    print("Ingresando fecha de primera consulta......")
    time.sleep(2)
    fecha_primera_c = driver.find_element(By.ID, 'fecha_primera_consulta')
    fecha_primera_c.send_keys(fecha_p_c)
    est_salud_antc_cli =driver.find_element(By.XPATH, "//*[@id='select2-id_institucion_primera_consulta-container']")
    est_salud_antc_cli.send_keys("Ejercicio libre de la profesión IV región")

