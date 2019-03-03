from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as u_req

my_url= "https://www.lazada.sg/catalog/?q=samsung+s10&_keyori=ss&from=input&spm=a2o42.home.search.go.654346b5zbD3j2"
client= u_req(my_url)
page_html= client.read()
client.close()
page_soup= soup(page_html,"html.parser")
page_soup.body
page_soup.findAll("div",{"class":"c2prKC"}) 