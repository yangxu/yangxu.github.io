import glob
import os
import platform
import codecs
from bs4 import BeautifulSoup

import os.path, time, datetime, pytz
import json
ignore_list = ['blog/index.html', 'learn/index.html']


def modification_date(filename):
    t = os.path.getmtime(filename)
    d = datetime.datetime.fromtimestamp(t)
    
    #utc_now = pytz.utc.localize(d)
    #pst_now = utc_now.astimezone(pytz.timezone("America/New_York"))
    
    #print utc_now
    #print pst_now
    
    return str(d)

def get_title_and_subtitle(filename):
    f=codecs.open(filename, 'r')
    soup = BeautifulSoup(f.read())
    title = soup.find('title').text
    subtitle = soup.findAll("h5", {"class": "subtitle"})
    if len(subtitle) > 0:
        subtitle = soup.findAll("h5", {"class": "subtitle"})[0].text
    else:
        subtitle = ''
    date = soup.findAll("p", {"class": "pull-right"})
    if len(date) > 0:
        date = soup.findAll("p", {"class": "pull-right"})[0].text.replace( 'Modification Date: ', '')
    else:
        date = ''
    return {"title":title, "subtitle":subtitle, 'date': date}

def to_index_json(folder, index_json):
    with open('%s/index.json'%folder, 'w') as outfile:
        json.dump(index_json, outfile)


a = glob.glob("blog/*.html")

index_json = []

for i in ignore_list:
    try:
        a.remove(i)
    except:
        pass

for i in a:
    title_and_subtitle = get_title_and_subtitle(i)
    if title_and_subtitle['date'] == '':
       result = {"filename": i, "date": modification_date(i), 'title': title_and_subtitle['title'], 'subtitle': title_and_subtitle['subtitle']}
    else:
       result = {"filename": i, "date": title_and_subtitle['date'], 'title': title_and_subtitle['title'], 'subtitle': title_and_subtitle['subtitle']}
    index_json.append(result)

print index_json
to_index_json('blog', index_json)


a = glob.glob("learn/*.html")

index_json = []

for i in ignore_list:
    try:
        a.remove(i)
    except:
        pass

for i in a:
    title_and_subtitle = get_title_and_subtitle(i)
    if title_and_subtitle['date'] == '':
       result = {"filename": i, "date": modification_date(i), 'title': title_and_subtitle['title'], 'subtitle': title_and_subtitle['subtitle']}
    else:
       result = {"filename": i, "date": title_and_subtitle['date'], 'title': title_and_subtitle['title'], 'subtitle': title_and_subtitle['subtitle']}
    index_json.append(result)

print index_json
to_index_json('learn', index_json)


