import Database
import InformationCollection
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import config


import time

import CompanyCollection

if __name__ == "__main__":
    collector = InformationCollection.Collector()
    driver = InformationCollection.WebDriver()

    db = Database.Database()

    db.openConnection()

    # db.client[config.DB_NAME]['jobs position'].drop()

    url = 'https://uk.indeed.com/jobs?q=data+scientist&sc=0bf%3Aexrec%28%29%3B&sort=date&vjk=ac6474397840972d'

    domain = "https://" + urlparse(url).netloc

    driver.start_dynamic_webdriver()

    driver.navigate_webpage_browser(url)

    time.sleep(1.5)

    print(collector.retrieve_Postings_From_Page(driver.browser.page_source,db.get_data("website")[0],url))
    # soup = BeautifulSoup(driver.browser.page_source, 'html.parser')
    # while(soup.find('a',{'data-testid':"pagination-page-next"})):
    #     time.sleep(1.5)
        
    #     driver.navigate_webpage_browser(domain+soup.find('a',{'data-testid':"pagination-page-next"})['href'])
    #     db.insert_data("jobs position",collector.retrieve_Postings_From_Page(driver.browser.page_source,db.get_data("website")[0],url))
    #     soup = BeautifulSoup(driver.browser.page_source, 'html.parser')
    #     # time.sleep(5)
    #     # break
    

    # time.sleep(5)

    # time.sleep(5)
    # url = "https://en.wikipedia.org/wiki/Microsoft"
    
    # url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

    # nameURL ="wikipedia top 50"

    driver.close_browser()
    # print(collector.find_info(driver.navigate_To_Webpage(url),url))

    # companies = collector.go_through_list_companies(driver.navigate_To_Webpage(url),nameURL, url)

    # result = []
    # for comp in companies[nameURL]["companies"].keys():
    #     result.append(collector.find_info(driver.navigate_To_Webpage(companies[nameURL]["companies"][comp]),companies[nameURL]["companies"][comp]))


    # db.insert_data("website",result)
