from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as u_req

#ignore this please.
# my_url= "https://www.lazada.sg/catalog/?q=mechanical+keyboard&_keyori=ss&from=input&spm=a2o42.searchlist.search.go.68f45227ArOOJq"
# client= u_req(my_url)
# page_html= client.read()
# client.close()
# page_soup= soup(page_html,"html.parser")
# # page_soup.body.div.div.div.div.div.div
# containers=page_soup.findAll("div",{"class":"c2prKC"}) 

my_url= "https://www.ebay.com.sg/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=samsung+s10&_sacat=0"
client= u_req(my_url)
page_html= client.read()
client.close()
page_soup= soup(page_html,"html.parser")
# page_soup.body.div.div.div.div.div.div
containers=page_soup.findAll("li",{"class":"sresult lvresult clearfix li shic"}) 

item="samsung galaxy s10"
lowest_price=9999999999
for  container in containers:
    name_str=container.img["alt"]
    name_str=name_str.lower()
    if item in name_str: #to check if the search parameter is indeed looking for samsung galaxy s10 related items
 
        price_str_before=container.span.text

        if "to" in price_str_before: #trying to remove everything after "to" because we want to focus on the cheapest price here
            pos_of_t= price_str_before.index("t")
            price_str_before=price_str_before[0:pos_of_t]
        price_str_after=""

        for i in price_str_before:
            if i.isdigit() or i==".":
                price_str_after+=i
                
        price=float(price_str_after)
        if price >=100 : #This is to sieve out the cheap priced accessories like casings and screen protectors to find the real phone
            if price <= lowest_price:
                lowest_price=price
print(lowest_price)

        
