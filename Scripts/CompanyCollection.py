from bs4 import BeautifulSoup
from urllib.parse import urlparse


import config

class CompanyCollector:

    def __init__(self) -> None:
        pass

    def go_through_list_companies(self,data,nameURL,url) -> dict:

        result = {}

        result[nameURL]= {}

        result[nameURL]["url"] = url

        result[nameURL]["companies"] = {}

        soup = BeautifulSoup(data, 'html.parser')
        

        # print(soup)

        tableValue =  soup.find('table', {"class":"wikitable sortable"})

        domain = "https://" + urlparse(url).netloc

        # print(tableValue)

        for row in tableValue.find_all("tr"):
                try:
                    tempname = row.find("td").text
                    tempurl = domain
                    for a in  row.find("td").find_all('a', href=True):
                        tempurl += a['href']

                    result[nameURL]["companies"][tempname] = tempurl
                        
                except:
                    continue
        return result


    def update_info(self, data):
        pass
        
    def find_info(self, data,url,haswiki=True):
        def get_table_info(data, tableClassName = "infobox vcard"):
            result = {}
            soup = BeautifulSoup(data, 'html.parser')
            tableValue =  soup.find('table', {"class":tableClassName})

            result['Company Name'] = soup.find('caption', {"class":"infobox-title fn org"}).text

            for row in tableValue.find_all("tr"):
                try:
                    if row.find('td',{"class": "infobox-data"}).find('div',{"class":"plainlist"}):
                        temp = []

                        for i in row.find('td',{"class": "infobox-data"}).find('div',{"class":"plainlist"}).find_all('li'):
                            temp.append(i.text)

                        result[row.find('th',{"class": "infobox-label"}).text] = temp
                    else:
                        if len(row.find('td',{"class": "infobox-data"}).text.split("\n"))>1:
                            temp = []
                            for i in row.find('td',{"class": "infobox-data"}).text.split("\n"):
                                if i != '':
                                    temp.append(i)
                            result[row.find('th',{"class": "infobox-label"}).text] = temp
                        else:
                            result[row.find('th',{"class": "infobox-label"}).text] = row.find('td',{"class": "infobox-data"}).text
                except:
                    continue
            return result
        result = get_table_info(data)
        result['has wiki page'] = haswiki
        result['wiki page'] = url
        result['is blocked'] = False
        return result
        pass