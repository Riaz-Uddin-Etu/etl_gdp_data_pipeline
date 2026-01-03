from bs4 import BeautifulSoup
import requests
import pandas as pd

def extract(url):
    # send a User-Agent header so Wikipedia treats like a normal browser.
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
        )
    } 
    
    response = requests.get(url, headers=headers) # response object
    response.raise_for_status() # check the response before parsing
    response = response.text # whole html page as text

    soup = BeautifulSoup(response, 'html.parser')
    table = soup.find_all('table')
    rows = table[2].find_all('tr')

    records = list()
    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 0:
            country = cols[0].get_text(strip=True)
            if '—' in cols[2]: continue # skip —  
            gdp = float(cols[2].get_text(strip=True).replace(',', ''))
            data_dict = {'Country': country, 'GDP_USD_millions': gdp}
            records.append(data_dict)
        else: continue

    df = pd.DataFrame(records)
    return df