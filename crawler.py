import requests
import re
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import locale
import logging
import json
import csv

def restaurant_names():
    result = []
    
    postal_codes = []
    ## Dummy postal code (can easily be extended)
    postal_codes.append('67551')
    
    for i in postal_codes:
        try:
            session = requests.Session()
            
            location_request = session.get('https://www.lieferando.de/' + str(i))
            location_parse = bs(location_request.text,"html.parser")
            location_name = location_parse.find_all("a", class_="restaurantname")
            
            location_list = []
            
            for idx, j in enumerate(location_name):
                name = j.text.strip()
                location_list.append(name)
            
            
        
        except Exception as e:
            print('Error: ',e)

    return location_list