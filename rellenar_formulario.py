from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from openpyxl import load_workbook
import time

from selenium.webdriver.remote.webelement import WebElement

# Driver para ingresar a la página inicial de EPI
driver = webdriver.Chrome(executable_path=r"C:\Users\luis.pizarro.a\PycharmProjects\Crear_ENO\chromedriver.exe")
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
folio = 28347736
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
# PRUEBAS PARA INGRESAR EL TIPO DE MUESTRA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# --Ingreso de la muestra a la plataforma
print("Ingresando datos de la muestra ")
tipo_paciente = driver.find_element(By.ID, 'tipo_especifico')
tipo_paciente.send_keys("IRA")
print("Esperando tipos de muestra......")
time.sleep(8)
tipo_muestra = driver.find_element(By.XPATH, "//*[@id='select_id_tipo_muestra']")
tipo_muestraOD = Select(tipo_muestra)
"""ddlist = tipo_muestraOD.options
print(len(ddlist))
for ele in ddlist:
    print("Value is: ", ele.text)"""
tipo_muestraOD.select_by_visible_text("Hisopado nasofaringeo")
print("Ingresando fecha de toma de la muestra......")
time.sleep(2)
"""tipo_muestra_selected = Select(driver.find_element(By.XPATH, "//*[@id='select_id_tipo_muestra']"))
opcion = tipo_muestra_selected.find_elements(By.TAG_NAME, 'option')
time.sleep(3)
for option in opcion:
    print("Valores: %s" % option.get_attribute("value"))
    option.click()
    time.sleep(1)
seleccionar = Select(driver.find_element(By.XPATH, "//*[@id='select_id_tipo_muestra']"))
seleccionar.select_by_value("10")
time.sleep(3)
# tipo_muestra_selected.select_by_value("3").click()
"""
fecha_toma_muestra = driver.find_element(By.ID, 'fecha_toma_muestra')
fecha_toma_muestra.send_keys("14-08-2022")
print("Ingresando resultado de antígeno.......")
time.sleep(2)
ag_positivo = driver.find_element(By.ID, 'tipo_otro_cultivo')
ag_positivo.send_keys("Positivo/reactivo")
print("Ingresando fecha de resultado.......")
time.sleep(2)
fecha_ag_positivo = driver.find_element(By.ID, 'fecha_resultado_otro_cultivo')
fecha_ag_positivo.send_keys("14-08-2022")
print("Ingresando detalle del antígeno")
time.sleep(2)
detalle_ag_positivo = driver.find_element(By.ID, 'resultado_otro_cultivo_detalle')
detalle_ag_positivo.send_keys("TEST ANTÍGENO")
# time.sleep(5)

# SECCIÓN 4 IDENTIFICACIÓN DE CONTACTOS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -Ir a la sección Identificación de contactos--------------------------------------------------------------------------
print("Ingresando a la sección 4...........")
seccion_4 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Identificación de contactos')
seccion_4.click()
time.sleep(3)

# SECCIÓN 5 CLASIFICACIÓN FINAL+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -Ir a la sección Clasificación final----------------------------------------------------------------------------------
print("Ingresando a la sección 5...........")
seccion_5 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Clasificación final')
seccion_5.click()
time.sleep(3)
# --Cambio en tipo de atención sección 5--------------------------------------------------------------------------------
# ---tipo_caso = driver.find_element(By.ID, 'tipo_caso_atencion_medica')
# ---tipo_caso.click()
# --Cambio en Etapa clinica sección 5 caso_descartado
descartado = driver.find_element(By.ID, 'caso_descartado')
descartado.click()
fecha_clasificacion = driver.find_element(By.ID, 'fecha_diagnostico')
fecha_clasificacion.send_keys("14-08-2022")
testlab = driver.find_element(By.ID, 'testlab')
testlab.click()
time.sleep(3)
# BOTON PARA VALIDAR LA NOTIFICACIÓN++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
validar = driver.find_element(By.XPATH, "//button[@type='submit'][@onclick='validar();']")
validar.click()
time.sleep(3)

"""# BOTÓN DE GUARDAR CAMBIOS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Guardar cambios
save = driver.find_element(By.ID, 'salvarcito')
save.click()
time.sleep(3)"""


#BOTÓN DE GUARDAR FORMULARIO++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# --Guardar formulario
# save_form = driver.find_element(By.ID, 'guardar_geo_mas_fomrulario')
save_form = driver.find_element(By.XPATH, "//*[@id='guardar_geo_mas_fomrulario']")
save_form.click()

"""# BOTÓN OK FINALIZAR++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ok = driver.find_element(By.XPATH, "//input[@type='button'][@type='button']")
ok.send_keys(Keys.ENTER)"""


"""
# ENTRAR AL HISTORIAL DE NOTIFICACIONES DE UN USUARIO A PARTIR DE SU RUT++++++++++++++++++++++++++++++++++++++++++++++++
rut_paciente = driver.find_element(By.ID, "n_identificacion")
rut_paciente.send_keys("192572843")
rut_paciente.send_keys(Keys.ENTER)
time.sleep(5)
"""

# fecha_notificacion = driver.find_element(By.NAME, "fecha_notificacion")
# fecha_notificacion.send_keys("2022-08-14")
# savebutton = driver.find_element(By.XPATH, "//button[@id='guardarcito'][@type='submit']")
# savebutton.click()


"""
# Formato para ingresar varios datos en un formulario. En este caso se hicieron pruebas con el formulario de login
for i in range(1, 3):
    user, password = nombres[f'A{i}:B{i}'][0]
    print(user.value, password.value)
    time.sleep(1)
    usuario = driver.find_element(By.NAME, "rut_usuario")
    usuario.send_keys(user.value)
    contrasena = driver.find_element(By.NAME, "password")
    contrasena.send_keys(password.value)
    time.sleep(1)
    # login = driver.find_element("id", "Ingresar").click()
    # loginbutton = driver.find_element(By., "btn btn-success btn-block btn-ingresar")
    loginbutton = driver.find_element(By.XPATH, "//input[@type='submit'][@type='submit']")
    loginbutton.click()
    
"""

# time.sleep(1)
# driver.quit()
