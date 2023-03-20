import json
def main():
    fptr = open("exercises/news.txt","r")
    file_text = fptr.read()
    fptr.close()

    file_pointer = open("exercises/subs.json","r")
    new_news = json.load(file_pointer)
    fptr = open("exercises/subs.json","r")
    for k,v in new_news.items():
        file_text = file_text.replace(k,v) 
    file_pointer.close()

    file_new = open("excersise/better_news.json", "r")
    file_new.write(new_news)
    file_new.close()



main()