from selenium import webdriver
import time
import xlsxwriter
from datetime import  date




def start(site):
    decreto = []
    emenda = []
    data = []
    elementsA = []
    elementsP = []
    elementsDD = []
    web = webdriver.Chrome()
    web.get(site)                                                              # abre o site
    t = web.find_element_by_xpath('//*[@id="ACERVO"]/ul/li[3]').text           #pega o numero de páginas
    t = int(t.split("de ", 1)[1])                                              # retira apenas o número da página
    for i in range(0, t):
        elementsP = web.find_elements_by_tag_name('p')
        elementsA = web.find_elements_by_tag_name('a')                         # pega elementos da página com tag a
        elementsDD = web.find_elements_by_class_name('hora2')
        #print(elementsDD)
        for elem in elementsDD:
            data.append(elem.text)
        for elem in elementsP:
            emenda.append(elem.text)
        for elem in elementsA:
            if(elem.text.find('Decreto Normativo') != -1):                     # verifica se esse elemento serve, é um texto de título de decreto
                decreto.append(elem.text)                                      # se sim, é adicionado a uma lista
        if(i >= t-1): 
            break                                                              # não pode haver o click de prox pagina para a ultima
        else:
            web.find_element_by_xpath('//*[@id="ACERVO"]/ul/li[4]/a').click()  #clicka para próxima página
    return decreto, emenda, data

def gerarExcel (decreto, emenda, datas, ano):
    today = date.today()
    today = str(today) +str(ano)+'.xlsx'
    with xlsxwriter.Workbook(today) as workbook:
        worksheet = workbook.add_worksheet()
        cont = 0
        for row_num, data in enumerate(decreto):
            print(row_num)#, str(data))
            for i in range(0, 1):
                    worksheet.write_string(row_num, i , str(decreto[cont]))
                    worksheet.write_string(row_num, i + 1 , str(emenda[cont]))
                    worksheet.write_string(row_num, i + 2 , str(datas[cont]))
                    cont = cont + 1
            if row_num == (len(decreto)/2-1):
                break    




if __name__ == '__main__':
    decreto = []
    emenda = []
    data = []
    elements = []
    ano = 2000
    number = 192
    for elem in range(0,22):
        site = 'http://www.gabinetecivil.rn.gov.br/Conteudo.asp?TRAN=PASTAC&TARG=2'+str(number)+'&ACT=&PAGE=&PARM=&LBL='
        decreto, emenda, data = start(site)
        gerarExcel(decreto, emenda, data, ano)
        ano = ano + 1
        number = number + 1


