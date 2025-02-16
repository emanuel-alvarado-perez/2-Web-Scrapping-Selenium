from selenium import webdriver
#Solo aplica para Local
#from selenium.webdriver.chrome.service import Service
#service = Service('C:\chromedriver.exe')
import time
from selenium.webdriver.common.keys import Keys
import datetime as dt

def get_driver():
  # Configuración de parametros iniciales
  options=webdriver.ChromeOptions() #Version Replit

  options.add_argument("disable-infobars") #Deshabilitar msj de info 
  options.add_argument("start-maximized") #Maximizar pantalla
  options.add_argument("disable-dev-shm-usage") #Evitar errones linux
  options.add_argument("no-sandbox") #Mayores permisos en el sitio web
  
  #Evita que Selenium sea identificado por el Navegador
  options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
  options.add_argument("disable-blink-features=AutomationControlled") 

  #Inicializar clase Driver con opciones seteadas
  driver=webdriver.Chrome(options=options)
  #driver=webdriver.Chrome(service=service,options=options) Para Local
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  """Extraer solamente la temperatura"""
  output=float(text.split(":")[1])
  return output

def main_webScraping():
  driver=get_driver()
  time.sleep(2)
  #Buscar un texto especifico
#  element=driver.find_element("xpath","/html/body/div[1]/div/h1[1]")
  element=driver.find_element("xpath","/html/body/div[1]/div/h1[2]") #Inspect, Copy Full Xpath
  return clean_text(element.text)

"""Ejecucion Primera Parte"""
#print(main_webScraping())

def get_driver_LoginApp():
  # Configuración de parametros iniciales
  options=webdriver.ChromeOptions() #Version Replit

  options.add_argument("disable-infobars") #Deshabilitar msj de info 
  options.add_argument("start-maximized") #Maximizar pantalla
  options.add_argument("disable-dev-shm-usage") #Evitar errones linux
  options.add_argument("no-sandbox") #Mayores permisos en el sitio web

  #Evita que Selenium sea identificado por el Navegador
  options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
  options.add_argument("disable-blink-features=AutomationControlled") 

  #Inicializar clase Driver con opciones seteadas
  driver=webdriver.Chrome(options=options)
  #driver=webdriver.Chrome(service=service,options=options) Para Local
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver


def main_LoginApp():
  driver=get_driver_LoginApp()  
  driver.find_element(by="id",value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id",value="id_password").send_keys("automatedautomated"+Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
  time.sleep(2)
  print(driver.current_url)

"""Ejercicio Segunda Parte"""
#print(main_LoginApp())


def get_driver_Exercise1():
  # Configuración de parametros iniciales
  options=webdriver.ChromeOptions() #Version Replit

  options.add_argument("disable-infobars") #Deshabilitar msj de info 
  options.add_argument("start-maximized") #Maximizar pantalla
  options.add_argument("disable-dev-shm-usage") #Evitar errones linux
  options.add_argument("no-sandbox") #Mayores permisos en el sitio web

  #Evita que Selenium sea identificado por el Navegador
  options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
  options.add_argument("disable-blink-features=AutomationControlled") 

  #Inicializar clase Driver con opciones seteadas
  driver=webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

def create_file(fileName,text):
  with open(fileName, "w") as file:
    file.write(text)
  file.close()


def main_Exercise1():
  driver=get_driver_LoginApp()  

  # Ingresar credenciales
  driver.find_element(by="id",value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id",value="id_password").send_keys("automatedautomated"+Keys.RETURN)
  time.sleep(2)

  # Hacer click en el boton de "Home"
  driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
  time.sleep(2)

  while True:
    # Extraer texto de la temperatura
    temperatura=driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]").text
    temperatura=clean_text(temperatura)
  
    # Crear nuevo archivo TXT para guardar el valor
    timestr = time.strftime("%Y%m%d-%H%M%S")
    fileName=timestr+".txt"
    text="Fecha: "+timestr+" "+"Temperatura: "+str(temperatura)
    create_file(fileName,text)
    
    print("Fecha: "+timestr+" "+"Temperatura: "+str(temperatura))
    

    time.sleep(2)
      
"""Ejercicio Practico"""
print(main_Exercise1())
