from bs4 import BeautifulSoup
import requests
from mdutils.mdutils import MdUtils
from mdutils import Html
from duckduckgo_search import DDGS

URL = "https://www.tiobe.com/tiobe-index/"
page = requests.get(URL)

site = BeautifulSoup(page.text, 'html.parser')


table = site.find("tbody")

resultTable = []
for i in range(4, len(table.find_all("td"))):
    resultTable.append(table.find_all("td")[i].text)

listaNazwa = 'list'
textLink = 'lista'


mainPage = MdUtils(file_name='index', title='Popularne języki programowania')

mainPage.new_header(level=1, title='Języki programowania')

mainPage.new_paragraph("Ważne dla każdego programisty, który właśnie wchodzi na rynek pracy, jest wybranie odpowiedniego języka programowania. "
                     "Dlatego prezentuję skróconą listę najbardziej popularnych języków programowania.")

#mainPage.new_line(mainPage.new_inline_link(link=listaNazwa + '.md', text=textLink))

mainPage.new_header(level=1, title='lista')
for i in range(5):
    with DDGS() as ddgs:
        results = ddgs.text(resultTable[7 * i] + " programming", max_results=5)
        print(next(results))
        mainPage.new_line(mainPage.new_inline_link(link=next(results)['href'], text='link do strony o ' + resultTable[7 * i]))

    mainPage.new_header(level=2, title=resultTable[7 * i])
mainPage.create_md_file()

#listPage = MdUtils(file_name=listaNazwa, title='Skrócona lista najbardziej popularnych języków programowania')

#listPage.new_header(level=1, title='lista')

#for i in range(5):
#    listPage.new_header(level=2, title=resultTable[7 * i])

#listPage.create_md_file()

