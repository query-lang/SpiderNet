from SpiderWeb.data_types import *
from dataclasses import dataclass
import subprocess
from typing import TypeVar
import re
T=TypeVar('T')

@dataclass
class GenSpider:
    """
    The class for Scraping the web. It has 6 functions . Instantiate the class with the url of the website.

    Example:
        .. code-block:: python
        from SpiderWeb import GenSpider
        spider = GenSpider("https:/www.example.com")
        
    """
    website:T


    def website_text(self):
        """
        This method returns the markup text of the website . 
        """
        website=subprocess.run(['curl', '-s', str(self.website)], stdout=subprocess.PIPE, text=True)
        return website.stdout
    def find_all_html_tags(self,tag,text=None):
        """
        This method finds all html tags passed in the parameter. If the tags are nested then 
        upon looping them you can add the 'text' keyword in the function to target the initial looped text
        """
        if text is None:
            text = self.website_text()
        pattern = f"<{tag}[^>]*>.*?</{tag}>"
        finder = re.findall(pattern, text, re.DOTALL)
        return finder
    def extract_text_from_html(self, html):
        """
        This method extracts text from the looped instance of the tag!
        """
        text = re.sub(r'<[^>]+>', '', html)
        return text.strip()
    def find_all_tags_by_classname(self, tag, class_name, text=None):
        """
        This method finds all html tags passed in the parameter with the given class only , also passed in the parameter. If the tags are nested then 
        upon looping them you can add the 'text' keyword in the function to target the initial looped text

        """
        if text is None:
            text = self.website_text()
        pattern = f'<{tag}[^>]*class="[^"]*\\b{class_name}\\b[^"]*"[^>]*>.*?</{tag}>'
        finder = re.findall(pattern, text, re.DOTALL)
        return finder
    def get_href_from_a_tags(self, text=None):
        """
        Returns a list of all href attributes 
        """
        if text is None:
            text = self.website_text()
        pattern = r'<a\s[^>]*href="([^"]*)"'
        hrefs = re.findall(pattern, text)
        return hrefs

    def get_src_from_img_tags(self, text=None):
        """
        Returns a list of all src attributes 
        """
        if text is None:
            text = self.website_text()
        pattern = r'<img\s[^>]*src="([^"]*)"'
        srcs = re.findall(pattern, text)
        return srcs
    
        


