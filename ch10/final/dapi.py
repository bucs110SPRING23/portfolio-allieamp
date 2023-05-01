import requests

class DAPI:
    def __init__(self):
        '''
        initializes the proxy class by establishing the base url and necessary additions
        args: (self) self refrences the instance of the class
        '''
        self.baseurl = "https://api.disneyapi.dev/"
        self.endpoint = 'character'
    def get(self,page):
        '''
        collects the API url you want to use and reuests it as json formay
        args: (int) page is the current page of the API data that you want to use
        return: (json) jsonurl is the API data in json format
        '''
        url = self.baseurl+self.endpoint+f'?page={page}'
        seturl = requests.get(url)
        jsonurl = seturl.json()
        return jsonurl
    def get_pages(self, response):
        '''
        figures out how many pages the API has
        args: (str) response is the section of the API formatting with information about the API's response formatting
        return: (int) how many pages the API has
        '''
        pages = response['info']['totalPages']
        return pages
    def parse_json(self, response):
        '''
        parses the json formatted data into a usable dictionary and uses that to make a list of characters who are listed in a film
        args: (str) response is the section of the API formatting with information about the API's response formatting
        return: (list) charlist is a list of every disney character credited in a movie
        '''
        charlist = []
        for item in response['data']:
            char = {
                'id': item['_id'],
                'name': item['name'],
                'films': item['films']
            }
            if item['films'] == []:
                pass
            else:
                charlist.append(char)
        return charlist
