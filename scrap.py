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

mainPage.new_paragraph("Ważne dla każdego programisty, który właśnie wchodzi na rynek pracy, jest wybranie odpowiedniego języka programowania. "
                     "Dlatego prezentuję skróconą listę najbardziej popularnych języków programowania.")

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
for i in range(5):
    mainPage.new_header(level=2, title=resultTable[7 * i])
    with DDGS() as ddgs:
        results = ddgs.text(resultTable[7 * i] + " programming wikipedia", max_results=5)
        mainPage.new_paragraph(opisy[i]);
        mainPage.new_line(mainPage.new_inline_link(link=next(results)['href'], text='link do strony wikipedii o ' + resultTable[7 * i]))

mainPage.new_line('\n --- \n')
mainPage.new_line('źródło: ' + mainPage.new_inline_link(link='https://www.tiobe.com/tiobe-index/', text='Strona tiobe' ))
mainPage.create_md_file()

#listPage = MdUtils(file_name=listaNazwa, title='Skrócona lista najbardziej popularnych języków programowania')

#listPage.new_header(level=1, title='lista')

#for i in range(5):
#    listPage.new_header(level=2, title=resultTable[7 * i])

#listPage.create_md_file()

