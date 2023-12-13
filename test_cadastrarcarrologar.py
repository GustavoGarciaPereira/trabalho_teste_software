import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestCadastrarCarroLogar():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_cadastrar_carro_logar(self):
        # Navegar para a página inicial
        self.driver.get("http://localhost:4200/welcome")
        self.driver.set_window_size(1920, 1080)

        # Realizar operações na página
        time.sleep(2)
        self.driver.find_element(By.ID, "cdca").click()
        self.driver.find_element(By.ID, "password").send_keys("%mC>)9's#:EsQ>z")
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("gustavo1")
        self.driver.find_element(By.CSS_SELECTOR, "app-login").click()
        self.driver.find_element(By.ID, "password").send_keys("gustavo1")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "cdca").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "nome").send_keys("gustavo")
        self.driver.find_element(By.ID, "marca").send_keys("gustavo")
        self.driver.find_element(By.ID, "modelo").send_keys("gustavo")
        time.sleep(2)
        self.set_slider_value(By.ID, "price", 122)
        self.driver.find_element(By.ID, "url_imagem").send_keys("https://upload.wikimedia.org/wikipedia/commons/4/45/VW_K%C3%A4fer%2C_Bj._1958_%282015-09-12_3727_b2%29.JPG")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "list").click()

    def set_slider_value(self, by, slider_id, slider_value):
        slider = self.driver.find_element(by, slider_id)
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(slider_value, 0).release().perform()
