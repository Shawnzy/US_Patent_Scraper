#!/usr/bin/env python
import re
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup
import codecs
import string

f = open('Test.xml')
str_data = f.read()
f.close()

row = ''
index = 0
for x in re.finditer('</us-patent-grant>', str_data):
    #print x.end()
    patent = str_data[index:x.end()]
    soup = BeautifulSoup(patent, "html.parser")

    doc_num_tag = soup.find("us-patent-grant")
    doc_num = doc_num_tag.attrs['file']
    print doc_num
    for tables in soup.find_all('tables', recursive=True):
        tables.decompose()
    text_sections = soup.find_all(['p','claim-text'])
    full_text = ''
    for text in text_sections:
        y = text.get_text()
        full_text = full_text + y
        print "hi"
    #replace tabs and carriage returns with ' '
    printable = set(string.printable)
    full_text = filter(lambda x: x in printable, full_text)
    full_text = full_text.replace('\n', ' ')
    full_text = full_text.replace('\t', ' ')
    full_text = full_text.replace('\r', '')
    full_text = full_text.replace('\x0b', '')
    full_text = full_text.replace('\x0c', '')
    row = row + doc_num + '\t' + full_text + '\n'
    index = x.end() + 1
chars = []
for c in row:
    if c not in chars:
        chars.append(c)
    else:
        continue
print sorted(chars)
file = codecs.open('output.txt', 'w', 'utf-8')
file.write(row)
file.close()
    #full_text = text_sections.find(text=True, recursive=False)
   # ft = full_text.find(text=True, recursive=False)
   # print ft
   # full_text_array =[]
    #for text in text_sections:
    #    full_text_array.append(text.get_text(recursive=False))
    #full_text = ''.join(full_text_array)
    #print full_text
   # for x in soup.iter('p'):
    #    print x.get_text()
    #text = soup.get_text()

   # xml_data = et.fromstring(patnt)
    #doc_num = xml_data.attrib['file']
    #for p in xml_data.iter('p'):
     #   D = p.text_content()
      #  print D
    #for claim in xml_daa.iter('claim-test'):
     #   print claim.text
    #for x in patent_list:
     #   print x.find("./us-patent-grant").attrib['file'].text

    #patent.append(str_data[index:x.end()])

###xml_data = et.fromstring(str_data)

###patent_list = xml_data.findall("us-patent-grant")

###for x in patent_list:
   ### print x.find("./us-patent-grant").attrib['file'].text