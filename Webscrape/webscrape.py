from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as u_req

#This is my first attempt at webscraping(single page) its objective is to find the cheapest samsung galaxy s10 from ebay. I do realize that there are some limitations.
#1. Search isn't as dynamic (only searching for s10).
#2. Single page search only.
#3. I didn't take into account of the inconsistences in the class usages some items have class name "shic" towards the end of the class name and some items don't.


my_url= "https://www.ebay.com.sg/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=samsung+s10&_sacat=0"
client= u_req(my_url)
page_html= client.read()
client.close()
page_soup= soup(page_html,"html.parser")

containers=page_soup.findAll("li",{"class":"sresult lvresult clearfix li shic"}) 

item="samsung galaxy s10"
lowest_price=9999999999
for  container in containers:
    name_str=container.img["alt"]
    name_str=name_str.lower()
    if item in name_str: #to clean up search parameters and check if the search parameter is indeed looking for samsung galaxy s10 related items
 
        price_str_before=container.span.text

        if "to" in price_str_before: #trying to remove everything after "to" because we want to focus on the cheapest price here since Ebay has a price range for some items
            pos_of_t= price_str_before.index("t")
            price_str_before=price_str_before[0:pos_of_t]
        price_str_after=""

        for i in price_str_before:  #converting into a proper price string that can be changed to int type
            if i.isdigit() or i==".":
                price_str_after+=i
                
        price=float(price_str_after) 
        if price >=100 : #This is to sieve out the cheap priced accessories like casings and screen protectors to find the real phone
            if price <= lowest_price:
                lowest_price=price
print("Lowest price for Samsung Galaxy S10 is $" + str(lowest_price))

        
