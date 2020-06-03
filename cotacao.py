from selenium import webdriver
import time
import os


class cotacao:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'D:\Biblioteca Eng_WB\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe')
        driver = self.driver
        driver.get('https://br.tradingview.com/symbols/BMFBOVESPA-DOL1!/')
        time.sleep(5)
        
    def preco(self):    
        user_element = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]').text
        return user_element
        

valor=cotacao()
while True:
    preco = valor.preco()
    print(preco)
