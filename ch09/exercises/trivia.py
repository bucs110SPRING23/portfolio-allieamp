import requests

def main():
    response = requests.get("http://opentdb.com/api.php?amount=5&category=11")
    data = response.json()
    results = data["results"] #makes in indexable with premade dictionary
    print(response.text)
main()