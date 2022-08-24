from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import time

from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(executable_path=r"C:\Users\luis.pizarro.a\PycharmProjects\Crear_ENO\chromedriver.exe")
driver.get("https://tomademuestras.minsal.cl/?pid=RPT3&rptd=4a95abe2-5ccb-d9f4-a120-3c3c7d6e72e4")
time.sleep(3)

usuario = driver.find_element(By.NAME, "username")
usuario.send_keys("Reg_coquimbo")
contrasena = driver.find_element(By.NAME, "password")
contrasena.send_keys("minsal.seremi4")
contrasena.send_keys(Keys.ENTER)

# loginbutton = driver.find_element(By.XPATH, "//input[@type='submit'][@type='submit']")
#analizar = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
analizar = driver.find_element(By.CSS_SELECTOR, 'button.btn btn-primary')
analizar.click()
# fecha_desde = driver.find_element(By.NAME, "fvar_fecha_desde")
# fecha_desde.click()
# fecha_desde.send_keys(Keys.ENTER)
# analizar.click()

"""
# input class="form-control" type=date name="fvar_fecha_desde"
fecha_desde = driver.find_element(By.NAME, "fvar_fecha_desde")
fecha_desde.send_keys("14/08/2022")
fecha_hasta = driver.find_element(By.NAME, "fvar_fecha_hasta")
fecha_hasta.send_keys("15-08-2022")
analizar = driver.find_element(By.LINK_TEXT, 'Analizar')
analizar.click()
"""
"""
dob = driver.find_element_by_css_selector("input#DOB")
driver.execute_script("window.scrollBy(0, 400)")
driver.execute_script("arguments[0].removeAttribute('readonly')", dob)
driver.find_element_by_css_selector("input#DOB").send_keys("10/08/2019")
"""

"""
loginbutton = driver.find_element(By.XPATH, "//input[@type='button'][@type='button']")
loginbutton.click()
"""