import json
def main():
    text_fptr = open("news.txt","r").read().lower()
    subs_fptr = open("subs.json","r")
    subs = json.load(subs_fptr)

    for k, v in subs.items():
        text_fptr = text_fptr.replace(k,v) 

    fptr = open("better_news.txt", "w")
    fptr.write(text_fptr)
    fptr.close()

main()