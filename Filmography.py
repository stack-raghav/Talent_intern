import requests
from bs4 import BeautifulSoup
import pandas as pd

input_txt = input("Enter the name of actor:")
input_txt = input_txt.replace(" ","_")
try:
    URL = "https://en.wikipedia.org/wiki/" + input_txt.title()  +"_filmography"
    
    print(URL)
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    
    results = soup.find('table', class_='plainrowheaders')
    
    if results == None:
        URL = "https://en.wikipedia.org/wiki/" + input_txt.title()
        print(URL)
        page = requests.get(URL)
        
        soup = BeautifulSoup(page.content, "html.parser")
        
        results = soup.find('table', class_='wikitable')
        
    rows = results.find_all('tr')
    final_data = []
    for i in rows:
        table_data = i.find_all('td', scope = "row")
        if table_data == []:
            table_data = i.find_all('td')
        data = [j.text for j in table_data]
        final_data += data
    print(final_data)
    l = len(final_data)
    for i in range(l):
        print(final_data[l-1-i])
except:
    print("OHO! Try another name or check your spelling")