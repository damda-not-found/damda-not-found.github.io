from bs4 import BeautifulSoup
import requests
from mdutils.mdutils import MdUtils
from mdutils import Html
from duckduckgo_search import DDGS
import re

def progLangGet(name, url):
    page = requests.get(url)
    site = BeautifulSoup(page.text, 'html.parser')
    text = site.find("b").parent
    return re.sub("\[.*\]", "", text.text)



URL = "https://www.tiobe.com/tiobe-index/"
page = requests.get(URL)

site = BeautifulSoup(page.text, 'html.parser')


table = site.find("tbody")

resultTable = []
for i in range(4, len(table.find_all("td"))):
    resultTable.append(table.find_all("td")[i].text)

listaNazwa = 'list'
textLink = 'lista'

indexPage = MdUtils(file_name='index', title='Popularne języki programowania')

indexPage.new_paragraph("Ważne dla każdego programisty, który właśnie wchodzi na rynek pracy, jest wybranie odpowiedniego języka programowania. "
                     "Dlatego prezentuję skróconą listę najbardziej popularnych języków programowania.")

indexPage.new_line(indexPage.new_inline_link(link='main.md', text='lista'))

mainPage = MdUtils(file_name='main', title='Popularne języki programowania')


opisy = [
"Z wyraźną przewagą, Python plasuje się na pierwszym miejscu najpopularniejszych języków programowania. "
"Jest to od kilku lat najpopularniejszy język programowania i nic nie wskazuje na zmianę w przyszłych latach.",
"Następnym na liście jest C. Pomimo, że C jest już ponad 50 letnim językiem programowania to nadal jest używany wśród programistów.",
"C++ znajduje się tuż za swoim przodkiem, C, na liście najbardziej popularnych języków programowania. Oprócz składni języka C, C++ oferuje również możliwość programowania obiektowego"
" i metaprogramowania.",
"Java rzeczywiście jest językiem programowania. Należy do prywatnej firmy Oracle i jest tam dalej rozwijana.",
"Tak jak Java, C# jest językiem czysto obiektowym i znajduje się w rękach prywatnej korporacji, Microsoftu. Dlatego użytkownicy Linuxa zazwyczaj nie programują w C#."
]

mainPage.new_header(level=1, title='lista')
for i in range(4):
    mainPage.new_header(level=2, title=resultTable[7 * i])
    with DDGS() as ddgs:
        results = ddgs.text(resultTable[7 * i] + " programming wikipedia", max_results=5)
        wikiSite = next(results)['href']
        mainPage.new_paragraph(opisy[i]);
        mainPage.new_line(mainPage.new_inline_link(link=resultTable[7 * i] + '.md', text='link do strony o ' + resultTable[7 * i]))
        currentPage = MdUtils(file_name=resultTable[7 * i]+ '.md', title=resultTable[7 * i])
        currentPage.new_paragraph(progLangGet(resultTable[7 * i], wikiSite))
        currentPage.new_line('\n --- \n')
        currentPage.new_line('źródło: ' + mainPage.new_inline_link(link=wikiSite, text='Wikipedia' ))
        currentPage.create_md_file()

mainPage.new_line('\n --- \n')
mainPage.new_line('źródło: ' + mainPage.new_inline_link(link='https://www.tiobe.com/tiobe-index/', text='Strona tiobe' ))
mainPage.create_md_file()


