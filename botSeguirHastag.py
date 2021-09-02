from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
# driver=self.webdriver
# user = self.find_element_by_id("selUsers")
# for option in user.find_elements_by_tag_name("option"):
#    if option.text == "Admin, Ascender":
#       actionChains = ActionChains(driver)
class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('user-data-dir=C:/Users/igor/Documents/GitHub/flask-bot/Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self,hastag):
        self.chrome.get(hastag)

    def login(self):
        botaoEntrar = self.chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
        botaoEntrar.click()
    def agoran(self):
        agrn = self.chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        agrn.click()
    def seguir(self):
        self.chrome.find_element_by_class_name('sqdOP').click()
    def abrircurtir(self):
        postagens = self.chrome.find_elements_by_class_name('_9AhH0')
        lista = []
        for post in postagens:
            lista.append(post)
        lista[0].click()
        sleep(1)

    def bot(self):
        self.chrome.maximize_window()
        for i in range(0,50):
            pyautogui.click(x=1166, y=419)
            sleep(1)
            pyautogui.doubleClick(x=515, y=329)
            sleep(1)


