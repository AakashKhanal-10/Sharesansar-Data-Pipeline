import requests
from bs4 import BeautifulSoup


def fetch_raw_table_rows(url)-> list:
    url= "https://www.sharesansar.com/today-share-price"
    
    """
    Fetches raw HTML table rows from a NEPSE market page.

    Args:
        url: Target Sharesansar URL.

    Returns:
        List of BeautifulSoup <tr> elements.
    """
    
    # 1. Connect to the internet and fetch the page
    response=requests.get(url,timeout=10)
    
    # 2. Convert the raw response text into a searchable HTML soup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 3. Cut out the specific table element
    market_table=soup.find("table")
    
    # 4. Return all raw table rows if the table exists, otherwise return an empty list
    return market_table.find_all("tr") if market_table else []