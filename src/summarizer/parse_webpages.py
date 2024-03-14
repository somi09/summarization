from bs4 import BeautifulSoup
import requests

class WebpageParser:
    '''A class to parse webpages'''
    def handle_text_tags(self, soup) -> str:
        '''
        A function to handle text tags
        args: soup:BeautifulSoup 
        returns: article:str
        '''
        results = soup.find_all(['h1', 'p'])
        text = [result.text for result in results]
        article = ' '.join(text)
        return article
    
    def parse(self, url) -> str:
        '''
        A function to extract webpages and parse them
        args: url:str 
        returns: article:str
        '''
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        article = self.handle_text_tags(soup)
        return article