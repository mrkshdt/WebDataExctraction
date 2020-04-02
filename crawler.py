import requests
import re
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import locale
import logging
import json
import csv

def get_locations(location_name):
    location_list = []
    for idx, j in enumerate(location_name):
        name = j.text.strip()
        location_list.append(name)
    return location_list

def lieferando_crawler(a):
    
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
            if a == 'locations':
                restaurant_list = get_locations(location_name)
                return restaurant_list
            elif a == 'products':
                print('None')
            else:
                print('None')
            
        
        except Exception as e:
            print('Error: ',e)
