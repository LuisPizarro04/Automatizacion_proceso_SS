from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from openpyxl import load_workbook
import time

from selenium.webdriver.remote.webelement import WebElement

# Driver para ingresar a la página inicial de EPI
driver = webdriver.Chrome(executable_path=r"C:\Users\luis.pizarro.a\PycharmProjects\Auto_Descarte_Eno\chromedriver.exe")
driver.get("https://epivigila.minsal.cl/index.php/administracion/ver-formulario/50")
time.sleep(3)  # tiempo de carga
# Cargar el excel que tiene los datos de usuario (por ahora no se usa)
filesheet = "./User_Pass.xlsx"
wb = load_workbook(filesheet)
# hojas = wb.get_sheet_names()
# print(hojas)
# hojas = wb.sheetnames
# print(hojas)
# nombres = wb["Hoja1"]
# wb.close()

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
time.sleep(3)
print("Ingresando a la notificación....")

"""# PASOS PARA INGRESAR AL FORMULARIO PARA LA CREACIÓN DE UNA NOTIFICACIÓN+++++++++++++++++++++++++++++++++++++++++++++
digitar = driver.find_element(By.LINK_TEXT, 'Digitar')
digitar.click()
coronavirus = driver.find_element(By.PARTIAL_LINK_TEXT, "Coronavirus")
coronavirus.click()"""

# ENTRAR A LA NOTIFICACIÓN POR UN FOLIO /50/FOLIO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
notificacion = "https://epivigila.minsal.cl/index.php/administracion/ver-formulario/50/"
folio = 28453238
folio = folio + 50000
enlacenotificacion = notificacion + str(folio)
# print(enlacenotificacion)  # Prueba para saber si funciona la unión del link mas el folio
print("Ingresando a la sección 1...........")
# SECCIÓN 1 IDENTIFICACIÓN DEL CASO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -Ir a la sección Identificación del caso------------------------------------------------------------------------------
driver.get(enlacenotificacion)
time.sleep(3)



# SECCIÓN 2 ANTECEDENTES CLINICOS Y EPIDEMIOLOGICOS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -Ir a la sección Antecedentes clínicos y epidemiológicos--------------------------------------------------------------
print("Ingresando a la sección 2...........")
seccion_2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Antecedentes clínicos y epidemiológicos')
seccion_2.click()
time.sleep(3)

# SECCIÓN 3 DATOS LABORATORIO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -Ir a la sección Datos laboratorio------------------------------------------------------------------------------------
print("Ingresando a la sección 3...........")
seccion_3 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Datos laboratorio')
seccion_3.click()
time.sleep(3)
# PRUEBAS PARA INGRESAR EL TIPO DE MUESTRA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --Ingreso de la muestra a la plataforma
eliminar_muestra = driver.find_element(By.XPATH, "//*[@id='btn_eliminar_muestra_especifica']")
eliminar_muestra.click()
# //*[@id="btn_eliminar_laboratorio"]
print("Ingresando datos de la muestra ")
# Selección del tipo de paciente
tipo_paciente = driver.find_element(By.ID, 'tipo_especifico')
tipo_pacienteOD = Select(tipo_paciente)
tipo_pacienteOD.select_by_visible_text("IRAG")
tipo_pacienteOD.select_by_visible_text("IRA")
# tipo_paciente.send_keys("IRA")
# Selección del tipo de muestra
print("Esperando tipos de muestra......")
time.sleep(8)
tipo_muestra = driver.find_element(By.XPATH, "//*[@id='select_id_tipo_muestra']")
tipo_muestraOD = Select(tipo_muestra)
tipo_muestraOD.select_by_visible_text("Hisopado nasofaringeo")
# //*[@id='btn_eliminar_laboratorio']
