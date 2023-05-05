import requests

class HPAPI:
    def __init__(self):
        '''
        initializes the proxy class by establishing the base url and necessary additions
        args: (self) self refrences the instance of the class
        '''
        self.baseurl = "https://hp-api.onrender.com/api/"
        self.endpoint = 'characters'
    def get(self):
        '''
        collects the API url you want to use and reuests it as json formay
        args: (self) self refrences the instance of the class
        return: (json) jsonurl is the API data in json format
        '''
        url = self.baseurl+self.endpoint
        requrl = requests.get(url)
        jsonurl = requrl.json()
        return jsonurl
    def parse_json(self, response):
        '''
        parses the json formatted data into a usable dictionary and uses that to make a list of characters
        args: (str) response is the section of the API formatting with information about the API's response formatting
        return: (list) charlist is a list of every harry potter character
        '''
        charlist = []
        for item in response:
            char = {
                'id': item['id'],
                'name': item['name'],
            }
            charlist.append(char)
        return charlist
