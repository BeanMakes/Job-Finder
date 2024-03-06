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



    url = 'https://uk.indeed.com/jobs?q=data+scientist&sc=0bf%3Aexrec%28%29%3B&sort=date&vjk=ac6474397840972d'

    domain = "https://" + urlparse(url).netloc

    driver.start_dynamic_webdriver()

    driver.navigate_webpage_browser(url)

    time.sleep(1.5)

    print(collector.retrieve_Postings_From_Page(driver.browser.page_source,db.get_data("website")[0],url))
    

    driver.close_browser()
    
