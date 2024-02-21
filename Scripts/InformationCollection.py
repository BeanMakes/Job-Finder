from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

import config
import requests
opts = Options()


class Collector:
    """
    Class which contain logic for how we will use the webpage and extract the information out
    
    """


    def __init__(self):
        pass

    def retrieve_Postings_From_Page(self,dataString:str, dataClasses:dict) -> dict:
        """
        Function to retrieve all information that is relevent to the job posts from websites.

        Args: String, String
        Returns: Dict
        
        """

        soup = BeautifulSoup(dataString, 'html.parser')

        result = {"Title":[],"company":[], "date posted":[], "link":[],"description":[]}

        # print(dataString)

        for post in soup.find_all(dataClasses["post"]['type'],{dataClasses["post"]['id'],dataClasses["post"]['name']}):
            try:
                print(post.find("span", {'class':"css-qvloho eu4oa1w0"}).text)
                result["Title"].append(self.get_title(post,dataClasses['post']['title']['type'],dataClasses['post']['title']['id'],dataClasses['post']['title']['name']))
                result["date posted"].append(self.get_date_posted(post,dataClasses['post']['date posted']['type'],dataClasses['post']['date posted']['id'],dataClasses['post']['date posted']['name']))
                result["link"].append(self.get_link(post,dataClasses['post']['title']['type'],dataClasses['post']['title']['id'],dataClasses['post']['title']['name']))
                # result["description"].append(self.get_description(post,dataClasses['post']['title']['type'],dataClasses['post']['title']['id'],dataClasses['post']['title']['name']))
            except:
                print("Error")
        return result
    
    def get_title(self,postData:str,idType:str, type:str, name:str )->str:

        # print(idType)
        return postData.find(idType, {type:name}).text

    def get_date_posted(self, postData:str,idType:str, type:str, name:str)->str:
        # print(postData.find(idType, {type:name}))
        return postData.find(idType, {type:name}).text

    def get_link(self, postData:str,idType:str, type:str, name:str) ->str:
        return postData.find(idType, {type:name}).text

    def get_description(self, postData:str,idType:str, type:str, name:str)->str:
        return postData.find(idType, {type:name}).text


class WebDriver():
    """
    Class relating to the webdriver which will be used and automatically control where to go.
    
    """
    def __init__(self):
        pass

    def start_dynamic_webdriver(self):
        opts = Options()
        self.browser = Firefox(options=opts)


    def enter_text_box_search(self, searchText,idName="text-input-what"):
        search_form = self.browser.find_element(By.ID, idName)
        search_form.send_keys('Data Scientist')
        search_form.submit()
    
    def start_Session(self):
        self.s = requests.Session()
        self.s.headers.update({'User-Agent':config.USERAGENT})

    def navigate_webpage_browser(self,url):
        self.browser.get(url)
    
    def navigate_To_Webpage(self, url:str):
        return self.s.get(url=url).content
    
    def close_browser(self):
        self.browser.close()
        quit()
        
    def end_Session(self):
        self.s.close()
