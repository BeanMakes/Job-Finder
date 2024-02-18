import Database
import InformationCollection

import CompanyCollection

if __name__ == "__main__":
    collector = CompanyCollection.CompanyCollector()
    driver = InformationCollection.WebDriver()

    driver.start_Session()

    url = "https://en.wikipedia.org/wiki/Microsoft"
    
    print(collector.find_info(driver.navigate_To_Webpage(url),url))