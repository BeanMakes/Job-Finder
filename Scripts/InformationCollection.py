from bs4 import BeautifulSoup

import config
import requests


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

        result = {"Title":[], "date posted":[], "link":[],"description":[]}

        for post in soup.find_all(dataClasses["classname"]):
            result["Title"].append(self.postData(post,dataClasses['post']['title']['attr']))
            result["date posted"].append(self.get_date_posted(post,dataClasses['post']['date']['attr']))
            result["link"].append(self.get_link(post,dataClasses['post']['link']['attr']))
            result["description"].append(self.get_description(post,dataClasses['post']['description']['attr']))

        return result
    
    def get_title(self,postData:str,attr:str)->str:
        return postData.find(attr)

    def get_date_posted(self, postData:str,attr:str)->str:
        return postData.find(attr)

    def get_link(self, postData:str,attr:str) ->str:
        return postData.find(attr) 

    def get_description(self, postData:str,attr:str)->str:
        return postData.find(attr)


class WebDriver():
    """
    Class relating to the webdriver which will be used and automatically control where to go.
    
    """
    def __init__(self):
        self.header = config.header

    def start_Session(self):
        self.s = requests.Session()
        self.s.headers.update({'User-Agent':config.USERAGENT})
        
    def navigate_To_Webpage(self, url:str):
        return self.s.get(url=url).content
        
    def end_Session(self):
        self.s.close()
