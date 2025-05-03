from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Configurar Selenium
options = Options()
options.headless = True  # Para que no se muestre la ventana del navegador
service = Service('/usr/bin/geckodriver')  # Ruta estándar para GeckoDriver
driver = webdriver.Firefox(service=service, options=options)

# Navegar a LinkedIn y buscar trabajos
driver.get("https://www.linkedin.com")
time.sleep(5)  # Esperar a que la página cargue

# Aquí deberías manejar el inicio de sesión y otras acciones necesarias
# ...

# Supongamos que has iniciado sesión, ahora navega a la sección de trabajos
driver.get("https://www.linkedin.com/jobs")
time.sleep(10)  # Esperar a que la página de trabajos cargue

# Extraer información sobre trabajos disponibles (esto es solo un ejemplo básico)
job_elements = driver.find_elements(By.CSS_SELECTOR, "h3.job-result-card__title")
for job in job_elements:
    print(job.text)

# Cerrar el navegador
driver.quit()