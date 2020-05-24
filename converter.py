from PIL import Image
from io import BytesIO
import base64
from bs4 import BeautifulSoup


HtmlFile = open('inline.html', 'r')
source_code = HtmlFile.read()
HtmlFile.close()

soup = BeautifulSoup(source_code, "html.parser")

images = soup.findAll('img')
print(images)
sources = []
for i in images:
    sources.append(i['src'].encode('ascii','ignore'))
print(sources)

new_source_code = source_code

for i in sources:
    im = Image.open(i)
    buff = BytesIO()
    im.save(buff, format="png")
    imbase64 = base64.b64encode(buff.getvalue())
    encodedimage = "data:image/jpeg;base64, " + imbase64
    new_source_code = new_source_code.replace(i, encodedimage)

newHtmlFile = open('newfile64.html', 'w')
newHtmlFile.write(new_source_code)
