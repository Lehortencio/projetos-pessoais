from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time

# Configuração do ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Maximizar a janela do navegador
chrome_options.add_argument("--disable-notifications")  # Desabilitar notificações

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options)

# Função para fazer login no Instagram
def login_instagram(username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)  # Aguarda o carregamento da página
    
    # Localiza os campos de login e senha
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    
    # Preenche os campos de login e senha]
    time.sleep(25)
    username_input.send_keys(username)
    time.sleep(25)
    password_input.send_keys(password)
    
    # Submete o formulário de login
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Aguarda o login ser processado

# Função para buscar um perfil específico e acessar sua última foto
def acessar_ultima_foto(perfil):
    # Busca o perfil na barra de pesquisa
    time.sleep(10)
    perfil = driver.get(f"https://www.instagram.com/{perfil}/")
    time.sleep(30)
    

# Credenciais e perfil a serem acessados
username = "username" #usuario do instagram
password = "password" #seenha do instagram
perfil = "cristiano"  #perfil do instagram que deseja entrar

# Fluxo principal
try:
    login_instagram(username, password)
finally:
    driver.quit()