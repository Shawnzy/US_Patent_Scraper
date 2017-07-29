#!/usr/bin/env python
from datetime import datetime
import time
import urllib2
import urllib
from bs4 import BeautifulSoup
import zipfile
import os

## Create Current Date
Date = datetime.now();

## Read last updated date
f = open('Last_Update.txt');
Last_Update_str = f.read();
f.close()

## convert to date object
Last_Update = datetime.strptime(Last_Update_str, '%m/%d/%Y');

## open Reed Website
url = "http://patents.reedtech.com/pgrbft.php"
soup = BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")

## Extract all Tables
table = soup.findAll('table', attrs={'class': 'bulktable'})

## Go through each table
i = 0;
Continue = True;
while i < len(table) and Continue == True:
    s = table[i];

    ## Extract all rows of table
    Tbl = s.findAll('tr')

    ## Go through each row of table
    j = 1;
    while j < len(Tbl) and Continue == True:
        row = Tbl[j];
        row_parsed = row.findAll('td');  ##Parse Row Entries

        Zip_Date_str = row_parsed[2].get_text();  ## Get Upload Date on Entry
        Title = Zip_Date_str.replace('/','-');    ## Create Upload Date String Used as Title When Saved
        Zip_Date = datetime.strptime(Title, '%m-%d-%Y'); ## Change Data typ from string to Datetime
        urlD = 'http://patents.reedtech.com/' + row_parsed[0].find('a').get('href'); ## Get URL for Download

        ##Download is file if the file hasn't been downloaded before. If it has end download While loops
        if Zip_Date >= Last_Update:
            Zip_Path = "download\\" + Title + ".zip"
            urllib.urlretrieve(urlD, Zip_Path) ##Download file

            z = zipfile.ZipFile(Zip_Path)
            z.extractall('download\\') ##Extract Zip contents
            z.close()
            os.remove(Zip_Path) ##Delete Zip Folder
        else:
            Continue = False;

        j = j + 1;

    i = i +1;


f = open('Last_Update.txt', 'w');
f.write((time.strftime("%m/%d/%Y")))
f.close


