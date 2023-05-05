import hpapi
import dapi

def main():
    hp = hpapi.HPAPI()
    hplist = []
    hplist.extend(hp.parse_json(hp.get()))
    disney = dapi.DAPI()
    dlist = []
    data = disney.get(1)
    for i in range(1,disney.get_pages(data)+1):
        dlist.extend(disney.parse_json(disney.get(i)))
    print("There are",len(hplist),"characters in the Harry Potter Films")
    print("There are",len(dlist),"characters in Disney Films")

main()
