from selenium import webdriver
#Solo aplica para Local
#from selenium.webdriver.chrome.service import Service
#service = Service('C:\chromedriver.exe')
import time

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

def main():
  driver=get_driver()
  time.sleep(2)
  #Buscar un texto especifico
#  element=driver.find_element("xpath","/html/body/div[1]/div/h1[1]")
  element=driver.find_element("xpath","/html/body/div[1]/div/h1[2]") #Inspect, Copy Full Xpath
  return clean_text(element.text)

print(main())



