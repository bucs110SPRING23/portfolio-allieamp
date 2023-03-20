import json
def main():
    fptr = open("exercises/news.txt","r")
    fptr.read()
    file_pointer = open("exercises/subs.json","r")
    new_news = json.loads(file_pointer)
    print(new_news, type(new_news))
    fptr = open("exercises/subs.json","w")
    for k,v in new_news:
        fptr.write(file_pointer[k] == file_pointer(v)) 
    
    fptr.close()
    file_pointer.close()


main()