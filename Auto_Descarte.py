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

"""# Cargar el excel que tiene los datos de usuario (por ahora no se usa)
filesheet = "C:\Carpeta_compartida\Scripts&DB\Bases\Auto_reporte_Descarte\Auto_Descarte_25-08-2022.xlsx"
wb = load_workbook(filesheet)
hojas = wb.get_sheet_names()
print(hojas)
hojas = wb.sheetnames
print(hojas)
nombres = wb["Datos"]
wb.close()"""

df = pd.read_excel('C:\Carpeta_compartida\Scripts&DB\Bases\Auto_reporte_Descarte\Auto_Descarte_25-08-2022.xlsx')
# df = pd.read_csv('C:\Carpeta_compartida\Scripts&DB\Bases\CSV_negativos_descartados\descartados_20220824.csv' )
print(df)

"""for i in range(len(df)):
    f_m = str(df.iloc[i]['fecha_toma_muestra'])
    dia = f_m[8:10]
    mes = f_m[5:7]
    agno = f_m[0:4]
    fecha = dia+"-"+mes+"-"+agno
    print(type(fecha))"""

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
time.sleep(5)

for i in range(len(df)):
    # ENTRAR A LA NOTIFICACIÓN POR UN FOLIO /50/FOLIO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    notificacion = "https://epivigila.minsal.cl/index.php/administracion/ver-formulario/50/"
    folio = df.iloc[i]['numero_folio']
    folio = folio + 50000
    enlacenotificacion = notificacion + str(folio)
    print("Ingresando a la sección 1...........")
    # SECCIÓN 1 IDENTIFICACIÓN DEL CASO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # -Ir a la sección Identificación del caso--------------------------------------------------------------------------
    driver.get(enlacenotificacion)
    time.sleep(4)
    prevision = driver.find_element(By.XPATH, "//*[@id='id_prevision_laboral']")
    # //*[@id="select2-id_prevision_laboral-container"]
    # //*[@id='select2-id_prevision_laboral-container']
    # //*[@id="id_prevision_laboral"]
    # /html/body/span/span
    # /html/body/span/span/span[1]/input
    # //*[@id="select2-id_prevision_laboral-results"]
    # prevision.get_property("title")
    # print("EL ELEMENTO ES", prevision)
    # previsionOD = Select(prevision)
    #ddlist = previsionOD.options
    #print(len(ddlist))
    #for ele in ddlist:
     #   print("Value is: ", ele,"->",ele.text)
    # previsionOD.select_by_visible_text("DESCONOCIDO")
    prevision.send_keys("DESCONOCIDO")

    break
    try:
        prevision = driver.find_element(By.XPATH, "//*[@id='id_prevision_laboral'']")
        # //*[@id='select2-id_prevision_laboral-container']
        # //*[@id="id_prevision_laboral"]
        # prevision.get_property("title")
        # print("EL ELEMENTO ES", prevision)
        previsionOD = Select(prevision)
        previsionOD.select_by_visible_text("DESCONOCIDO")
        # prevision.send_keys("DESCONOCIDO")

    except:

        # SECCIÓN 2 ANTECEDENTES CLINICOS Y EPIDEMIOLOGICOS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # -Ir a la sección Antecedentes clínicos y epidemiológicos------------------------------------------------------
        print("Ingresando a la sección 2...........")
        seccion_2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Antecedentes clínicos y epidemiológicos')
        seccion_2.click()
        time.sleep(3)
        # Ingreso de la fecha de primera consulta
        print("Ingresando fecha de primera consulta......")
        time.sleep(2)
        fecha_primera_c = driver.find_element(By.ID, 'fecha_primera_consulta')
        f_p_c = str(df.iloc[i]['fecha_toma_muestra'])
        dia = f_p_c[8:10]
        mes = f_p_c[5:7]
        agno = f_p_c[0:4]
        fecha_p_c = dia + "-" + mes + "-" + agno
        fecha_primera_c.send_keys(fecha_p_c)
        # SECCIÓN 3 DATOS LABORATORIO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # -Ir a la sección Datos laboratorio--------------------------------------------------------------------------------
        print("Ingresando a la sección 3...........")
        seccion_3 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Datos laboratorio')
        seccion_3.click()
        time.sleep(3)
        # PRUEBAS PARA INGRESAR EL TIPO DE MUESTRA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # --Ingreso de la muestra a la plataforma
        eliminar_muestra = driver.find_element(By.XPATH, "//*[@id='btn_eliminar_muestra_especifica']")
        eliminar_muestra.click()
        print("Ingresando datos de la muestra ")
        # Selección del tipo de paciente
        tipo_paciente = driver.find_element(By.ID, 'tipo_especifico')
        tipo_pacienteOD = Select(tipo_paciente)
        tipo_pacienteOD.select_by_visible_text("IRA")
        # tipo_paciente.send_keys("IRA")
        # Selección del tipo de muestra
        print("Esperando tipos de muestra......")
        time.sleep(8)
        tipo_muestra = driver.find_element(By.XPATH, "//*[@id='select_id_tipo_muestra']")
        tipo_muestraOD = Select(tipo_muestra)
        tipo_muestraOD.select_by_visible_text("Hisopado nasofaringeo")
        # Ingreso de la fecha de toma de muestra
        print("Ingresando fecha de toma de la muestra......")
        time.sleep(2)
        fecha_toma_muestra = driver.find_element(By.ID, 'fecha_toma_muestra')
        f_m = str(df.iloc[i]['fecha_toma_muestra'])
        dia = f_m[8:10];
        mes = f_m[5:7];
        agno = f_m[0:4];
        fecha_toma = dia + "-" + mes + "-" + agno
        fecha_toma_muestra.send_keys(fecha_toma)
        # Ingresando antigeno como tipo otro cultivo
        print("Ingresando resultado de antígeno.......")
        time.sleep(2)
        ag_positivo = driver.find_element(By.ID, 'tipo_otro_cultivo')
        ag_positivo.send_keys("Negativo/No reactivo")
        # Ingresando la fecha de resultado del antígeno
        print("Ingresando fecha de resultado.......")
        time.sleep(2)
        fecha_ag_positivo = driver.find_element(By.ID, 'fecha_resultado_otro_cultivo')
        f_r = str(df.iloc[i]['fecha_toma_muestra'])
        dia = f_r[8:10];
        mes = f_r[5:7];
        agno = f_r[0:4];
        fecha_resultado = dia + "-" + mes + "-" + agno
        fecha_ag_positivo.send_keys(fecha_resultado)
        # Ingresando detalle de la muestra " Teste antígeno"
        # print("Ingresando detalle del antígeno")
        # time.sleep(2)
        # detalle_ag_positivo = driver.find_element(By.ID, 'resultado_otro_cultivo_detalle')
        # detalle_ag_positivo.send_keys("TEST ANTÍGENO")
        # time.sleep(2)
        # SECCIÓN 4 IDENTIFICACIÓN DE CONTACTOS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # -Ir a la sección Identificación de contactos------------------------------------------------------------------
        print("Ingresando a la sección 4...........")
        seccion_4 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Identificación de contactos')
        seccion_4.click()
        time.sleep(3)
        # SECCIÓN 5 CLASIFICACIÓN FINAL+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # -Ir a la sección Clasificación final--------------------------------------------------------------------------
        print("Ingresando a la sección 5...........")
        seccion_5 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Clasificación final')
        seccion_5.click()
        time.sleep(3)
        # --Cambio en Etapa clinica sección 5 caso_descartado
        descartado = driver.find_element(By.ID, 'caso_descartado')
        descartado.click()
        fecha_clasificacion = driver.find_element(By.ID, 'fecha_diagnostico')
        f_c = str(df.iloc[i]['fecha_toma_muestra'])
        dia = f_c[8:10];
        mes = f_c[5:7];
        agno = f_c[0:4];
        fecha_clas = dia + "-" + mes + "-" + agno
        fecha_clasificacion.send_keys(fecha_clas)
        testlab = driver.find_element(By.ID, 'testlab')
        testlab.click()
        time.sleep(3)
        # BOTON PARA VALIDAR LA NOTIFICACIÓN++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        validar = driver.find_element(By.XPATH, "//button[@type='submit'][@onclick='validar();']")
        validar.click()
        time.sleep(3)
        """"# BOTÓN DE GUARDAR CAMBIOS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # Guardar cambios
            save = driver.find_element(By.ID, 'salvarcito')
            save.click()
            time.sleep(3)"""
        # BOTÓN DE GUARDAR FORMULARIO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # --Guardar formulario
        # save_form = driver.find_element(By.ID, 'guardar_geo_mas_fomrulario')
        save_form = driver.find_element(By.XPATH, "//*[@id='guardar_geo_mas_fomrulario']")
        save_form.click()
