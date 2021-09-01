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
    def __init__(self,login,senha,hastag):
        self.login = login
        self.senha = senha
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('user-data-dir=C:/Users/igor/Documents/GitHub/flask-bot/Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )



        sleep(2)
        self.chrome.get(f'https://www.instagram.com/explore/tags/{hastag}/')
        self.chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()
        sleep(2)
        self.chrome.find_element_by_name('username').send_keys(login)
        self.chrome.find_element_by_name('password').send_keys(senha)
        self.chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(3)
        self.chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    # def login(self):
    #     self.chrome.get('https://www.instagram.com/')

    def seguir(self):
        self.chrome.find_element_by_class_name('sqdOP').click()
    def abrircurtir(self):
        #div q tem as postagens da hastag EZdmt
        # class das hastag _9AhH0 tdas iguais _9AhH0
        # svg aria-label="Curtir"   /html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg
        # proiximo class coreSpriteRightPaginationArrow
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

if __name__=='__main__':
    chrome = ChromeAuto(login = input('Login: '),senha=input('Senha: ' ),hastag=input('buscar Hastag: '))

    chrome.seguir()
    chrome.abrircurtir()
    sleep(2)
    chrome.bot()

