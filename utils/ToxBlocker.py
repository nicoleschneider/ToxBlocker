def ParseInfoFromALink(link):
    import urllib
    import requests
    from bs4 import BeautifulSoup
    response1 = requests.get(link)
    print(response1
    if(response1.content == "Sorry, for some reason reddit can't be reached."):
       print("Try Again Later")
    else:
        dom1 = BeautifulSoup(response1.content,"lxml")
        dom1list=[]
        for p1 in dom1("p"):
            if(p1.text != "Sorry, for some reason reddit can't be reached."):
                dom1list.append(str(p1.text))
            else:
                print("Reddit Blocked the request, try again in a bit.")
        print(dom1list)
url1 = "https://www.reddit.com/r/facepalm/comments/3ymh8r/discussing_controversial_gender_issues_always/"
ParseInfoFromALink(url1)
