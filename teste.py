from selenium import webdriver
import time
import xlsxwriter
from datetime import  date




web = webdriver.Chrome()
web.get('http://adcon.rn.gov.br/ACERVO/gac/DOC/DOC000000000067297.PDF')
print(web.find_element_by_xpath('//*[@id="plugin"]').text)
