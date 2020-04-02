import requests
import re
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import locale
import logging
import json
import csv
## def products_instance():
    

def get_locations(location_name, option, session):
    
    restaurant_links = []
    location_list = []
    
    for idx, j in enumerate(location_name):
        name = j.text.strip()
        location_list.append(name)

        restaurant_links.append([j['href'],name])
        try:
            location_string = str(restaurant_links[idx][0])
            products_request = session.get('https://www.lieferando.de'+location_string)
                   
        except Exception as e:
            print('Error at restaurant: ', location_string, ' as ', e)
        
    if option == 'names':
        return location_list    
    else:
        print('Test')
    

def lieferando_crawler(option):
    
    ## Dummy postal code 
    ## User can give Postal Codes as input for the function e.g.
    postal_codes = []
    postal_codes.append('67551')
    
    ## Iterating over postal codes
    for i in postal_codes:
        try:
            session = requests.Session()
            
            ## Workflow to get data
            location_request = session.get('https://www.lieferando.de/' + str(i))
            location_parse = bs(location_request.text,"html.parser")
            location_name = location_parse.find_all("a", class_="restaurantname")
              
            ## User selection of which data is wanted
            
            result = get_locations(location_name, option, session)
            
            
        
        except Exception as e:
            print('Error: ',e)
    return result