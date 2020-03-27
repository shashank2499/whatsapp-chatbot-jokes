import requests 
from bs4 import BeautifulSoup   
def corona(state):
    extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
    URL = 'https://www.mohfw.gov.in/'
    SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed', 
                 'Foreign-Confirmed','Cured','Death']
    response = requests.get(URL).content
    soup = BeautifulSoup(response, 'html.parser')
    header = extract_contents(soup.tr.find_all('th'))
    stats = []
    all_rows = soup.find_all('tr')
    for row in all_rows:
        stat = extract_contents(row.find_all('td'))
        if stat:
            if len(stat) == 5:
                stat = ['', *stat]
                stats.append(stat)
            elif len(stat) == 6:
                stats.append(stat)
    stats[-1][1] = "Total Cases"
    stats.remove(stats[-1])
    flag=1
    for row in stats:
        if row[1]==state:
            result="State:{} Indians-Confirmed:{} Foreigners-Confirmed:{} Cured:{} Deaths:{}".format(row[1],row[2],row[3],row[4],row[5])
            flag=0
        if flag=1:
            result="not matching"
    return result
