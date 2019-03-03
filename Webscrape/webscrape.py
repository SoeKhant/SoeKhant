from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as u_req


#This is my first attempt at webscraping(single page) its objective is to find the cheapest samsung galaxy s10 from ebay. I do realize that there are some limitations.

#1. Single page search only.
#2. I didn't take into account of the inconsistences in the class usages some items have class name "shic" towards the end of the class name and some items don't.

#The function find_cheapest_price takes in 3 parameters
#my_url is the url of the page in ebay that you want to conduct a search from
#item is the name of the item that you want get
#price_floor is to set a lower limit to sieve out any accessories that are usually cheaper than the actual product, because one would only want the actual item.

def find_cheapest_price(my_url,item,price_floor):
    
    client= u_req(my_url)
    page_html= client.read()
    client.close()
    page_soup= soup(page_html,"html.parser")

    containers= page_soup.findAll("li",{"class":"sresult lvresult clearfix li shic"}) 
    # containers1= page_soup.findAll("li",{"class":"sresult lvresult clearfix li"})
    # containers= containers + containers1

    
    lowest_price= 9999999999999999
    for  container in containers:
        name_str= container.img["alt"]
        name_str= name_str.lower()
        if item in name_str: #to clean up search parameters and check if the search parameter is indeed looking for samsung galaxy s10 related items
        
            price_str_before=container.span.text

            if "to" in price_str_before: #trying to remove everything after "to" because we want to focus on the cheapest price here since Ebay has a price range for some items
                pos_of_t= price_str_before.index("t")
                price_str_before= price_str_before[0:pos_of_t]
            price_str_after= ""

            for i in price_str_before:  #converting into a proper price string that can be changed to int type
                if i.isdigit() or i== ".":
                    price_str_after+=i

            price=float(price_str_after) 
            if price >= price_floor : #This is to sieve out the cheap priced accessories like casings and screen protectors to find the real phone
                if price <= lowest_price:
                    lowest_price= price
    return (lowest_price)

# my_url= "https://www.ebay.com.sg/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=samsung+s10&_sacat=0"
# item="samsung galaxy s10"  
# price_floor= 100

my_url= "https://www.ebay.com.sg/sch/i.html?_odkw=dell&_osacat=0&_from=R40&_trksid=m570.l1313&_nkw=dell+xps+15&_sacat=0"
item= "dell xps 15"
price_floor= 1400
print("Lowest price for "+ item + " is $" + str(find_cheapest_price(my_url,item,price_floor)))

        

        
