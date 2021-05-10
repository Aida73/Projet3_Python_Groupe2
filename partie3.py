import requests
import re
#https://esp.com/
#get_urls('https://fr.wikipedia.org/wiki/Code_DTMF')
#"https://fr.besoccer.com/joueur/c-ronaldo-28185"



def get_pages(url):
    code_source = requests.get(url)
    return code_source.text


def get_emails(url):
    response = requests.get(url)
    lesemails=re.compile("[a-z][\w\.]+@[\w\.]*\.[a-z]*").findall(get_pages(url))
    if lesemails:
        return lesemails
    else:
        return "Pas d'email"  
    
    
def get_urls(url):
    lesurls = re.compile(r'href=[\'"]?([^\'" >]+)').findall(get_pages(url))
    if lesurls:
        urls = list(lesurls)
        for elt in list(urls):
            print(elt)
        return len(urls)
    else:
        return "Pas d'urls"
    
    
def get_tables(url):
    page = get_pages(url)
    return page[page.index('<table'):page.index('</table>')+8]