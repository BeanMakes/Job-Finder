# import Database
import InformationCollection

import time

import CompanyCollection

if __name__ == "__main__":
    collector = CompanyCollection.CompanyCollector()
    driver = InformationCollection.WebDriver()

    # db = Database.Database()

    # db.openConnection()

    driver.start_dynamic_webdriver()

    driver.navigate_webpage_browser('https://uk.indeed.com/')

    time.sleep(5)

    # url = "https://en.wikipedia.org/wiki/Microsoft"
    
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

    nameURL ="wikipedia top 50"

    driver.close_browser()
    # print(collector.find_info(driver.navigate_To_Webpage(url),url))

    # companies = collector.go_through_list_companies(driver.navigate_To_Webpage(url),nameURL, url)

    # result = []
    # for comp in companies[nameURL]["companies"].keys():
    #     result.append(collector.find_info(driver.navigate_To_Webpage(companies[nameURL]["companies"][comp]),companies[nameURL]["companies"][comp]))


    # db.insert_data(result)
