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
    try:
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

        if df.iloc[i]["prevision"] == 0:
            print("Ingresar Desconocido en prevision")
            prevision = driver.find_element(By.XPATH, "//*[@id='select2-id_prevision_laboral-container']")
            prevision.click()
            time.sleep(3)
            mov_lis = driver.find_element(By.XPATH, "//*[@id='select2-id_prevision_laboral-results']")
            mov_lis.find_element(By.XPATH, "//*[@id='select2-id_prevision_laboral-results']/li[7]").click()

        print("Resto del codigo")
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
        # SECCIÓN 3 DATOS LABORATORIO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # -Ir a la sección Datos laboratorio----------------------------------------------------------------------------
        print("Ingresando a la sección 3 del registro: ", i)
        seccion_3 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Datos laboratorio')
        seccion_3.click()
        time.sleep(3)
        # PRUEBAS PARA INGRESAR EL TIPO DE MUESTRA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # --Ingreso de la muestra a la plataforma
        eliminar_muestra = driver.find_element(By.XPATH, "//*[@id='btn_eliminar_muestra_especifica']")
        eliminar_muestra.click()
        # //*[@id="btn_eliminar_laboratorio"]
        print("Ingresando datos de la muestra ")
        # Selección del tipo de paciente
        tipo_paciente = driver.find_element(By.ID, 'tipo_especifico')
        tipo_pacienteOD = Select(tipo_paciente)
        time.sleep(2)
        tipo_pacienteOD.select_by_visible_text("IRAG")
        time.sleep(2)
        tipo_pacienteOD.select_by_visible_text("IRA")
        # tipo_paciente.send_keys("IRA")
        # Selección del tipo de muestra
        print("Esperando tipos de muestra......")
        time.sleep(12)
        tipo_muestra = driver.find_element(By.XPATH, "//*[@id='select_id_tipo_muestra']")
        tipo_muestraOD = Select(tipo_muestra)
        tipo_muestraOD.select_by_visible_text("Hisopado nasofaringeo")
        # Ingreso de la fecha de toma de muestra
        print("Ingresando fecha de toma de la muestra......")
        time.sleep(2)
        fecha_toma_muestra = driver.find_element(By.ID, 'fecha_toma_muestra')
        fecha_toma_muestra.send_keys(fecha_p_c)
        # Ingresando antigeno como tipo otro cultivo
        print("Ingresando resultado de antígeno.......")
        time.sleep(2)
        ag_positivo = driver.find_element(By.ID, 'tipo_otro_cultivo')
        ag_positivo.send_keys("Negativo/No reactivo")
        # Ingresando la fecha de resultado del antígeno
        print("Ingresando fecha de resultado.......")
        time.sleep(2)
        fecha_ag_positivo = driver.find_element(By.ID, 'fecha_resultado_otro_cultivo')
        fecha_ag_positivo.send_keys(fecha_p_c)
        # SECCIÓN 4 IDENTIFICACIÓN DE CONTACTOS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # -Ir a la sección Identificación de contactos------------------------------------------------------------------
        print("Ingresando a la sección 4 del registro: ", i)
        seccion_4 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Identificación de contactos')
        seccion_4.click()
        time.sleep(3)
        # SECCIÓN 5 CLASIFICACIÓN FINAL+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # -Ir a la sección Clasificación final--------------------------------------------------------------------------
        print("Ingresando a la sección 5 del registro: ", i)
        seccion_5 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Clasificación final')
        seccion_5.click()
        time.sleep(3)
        # --Cambio en Etapa clinica sección 5 caso_descartado
        descartado = driver.find_element(By.ID, 'caso_descartado')
        descartado.click()
        fecha_clasificacion = driver.find_element(By.ID, 'fecha_diagnostico')
        fecha_clasificacion.send_keys(fecha_p_c)
        testlab = driver.find_element(By.ID, 'testlab')
        testlab.click()
        time.sleep(3)
        # BOTON PARA VALIDAR LA NOTIFICACIÓN++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        validar = driver.find_element(By.XPATH, "//button[@type='submit'][@onclick='validar();']")
        validar.click()
        time.sleep(3)
        # BOTÓN DE GUARDAR FORMULARIO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # --Guardar formulario
        # save_form = driver.find_element(By.ID, 'guardar_geo_mas_fomrulario')
        save_form = driver.find_element(By.XPATH, "//*[@id='guardar_geo_mas_fomrulario']")
        save_form.click()
    except :
        print("Siguiente")
        # driver.refresh()
