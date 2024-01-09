from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Chrome()

driver.get('https://lista.mercadolivre.com.br/lamas#D[A:lamas,L:undefined]')

whiskys = driver.find_elements(By.XPATH, '//h2[@class="ui-search-item__title"]')
prices = driver.find_elements(By.XPATH, 
                              '//span[@class="andes-money-amount__fraction"]')

wb = openpyxl.Workbook()
wb.create_sheet('mercadoLivre')
sheet_ml = wb['mercadoLivre']

for whisky, price in zip(whiskys, prices):
  sheet_ml.append([whisky.text, price.text])

wb.save('automacao/02/mercado_livre.xlsx')