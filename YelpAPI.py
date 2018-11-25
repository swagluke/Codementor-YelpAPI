
# coding: utf-8

# In[ ]:

# Yelp API
# https://github.com/gfairchild/yelpapi
# Need to run following code in terminal
# pip install yelpapi


# In[9]:

import pandas as pd
from pprint import pprint
from yelpapi import YelpAPI


# In[41]:

# Need to get Dev API Key from Yelp
# https://www.yelp.com/login?return_url=%2Fdevelopers%2Fv3%2Fmanage_app

# Inserting API into Yelp request
yelp_api = YelpAPI("")


# In[42]:

pprint(response)


# In[54]:

# Loading Locations data from CSV File
Locations = pd.read_csv("Location.csv")

# Loading Merchants data from CSV File
Merchants = pd.read_csv("Merchant.csv")


# In[55]:

Locations.head()


# In[56]:

Merchants.head()


# In[60]:

Name = []
Categories = []
Address = []
Url = []
Phone = []
Price = []
Rating = []
for Location in Locations['Locations']:
    for Merchant in Merchants['Merchants']:
        response = yelp_api.search_query(term = Merchant, location= Location, sort_by='rating', limit = 20)
        for business in response.get('businesses'):
            Name.append(business.get('name'))
            Categories.append(business.get('categories'))
            Address.append(business.get('location').get('display_address'))
            Url.append(business.get('url'))
            Phone.append(business.get('phone'))
            Price.append(business.get('price'))
            Rating.append(business.get('rating'))


# In[61]:

Results = pd.DataFrame()
Results['Name'] = Name
Results['Categories'] = Categories
Results['Address'] = Address
Results['Url'] = Url
Results['Phone'] = Phone
Results['Price'] = Price
Results['Rating'] = Rating


# In[62]:

Results


# In[63]:

Results.to_excel("Results.xlsx")


# In[ ]:



