from Packages import *

print('Iniciando robô... \n')

#workbook = xlrd.open_workbook('dom.xlsx')
#sheet = workbook.sheet_by_index(0)
#dominios = []
#for lin in range(len(sheet)):
#    dominios.append(sheet.cell_value(lin, 0))

db = open('doms.txt', 'r')

dominios = []
for lin in db:
    stripped_line = lin.strip()
    dominios.append(stripped_line)

s = Service('...//chromedriver.exe') #!!!Chromedriver path here!!!
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service = s, options=options)
driver.get('https://registro.br/')

output = open('output.txt', 'w')

for dominio in dominios:

    pesquisa = driver.find_element(By.ID,'is-avail-field')
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)

    resultados = driver.find_elements(By.TAG_NAME, 'strong')
    print('Domínio %s %s.' % (dominio, resultados[4].text))
    output.write('Domínio %s %s. \n' % (dominio, resultados[4].text))
    time.sleep(2)

output.close()
driver.close()