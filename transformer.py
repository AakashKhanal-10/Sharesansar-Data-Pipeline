import pandas as pd
from extractor import fetch_raw_table_rows

def clean_market_data(rows):
    if not rows:
        return pd.DataFrame()
    headers=[th.get_text(strip=True) for th in rows[0].find_all("th")]
    raw_matrix=[]
    for row in rows[1:]:
        cells=[td.get_text(strip=True) for td in row.find_all("td")]
        if cells:
            raw_matrix.append(cells)
    df=pd.DataFrame(raw_matrix, columns=headers)
    numeric_cols=['LTP', 'Diff %', 'Open', 'High', 'Low', 'Vol', 'Turnover']
    for col in numeric_cols:
        if col in df.columns:
            df[col]= df[col].astype(str).str.replace(',', '',regex=False)
            df[col]=pd.to_numeric(df[col], errors='coerce')
    df=df.dropna(subset=["Symbol"])
    return df

if __name__=="__main__":
    url = "https://www.sharesansar.com/today-share-price"
    print("Fetching data from Sharesansar...")
    raw_rows = fetch_raw_table_rows(url)
    if raw_rows:
        print(f"Successfully fetched {len(raw_rows)} rows. Cleaning data...")
        cleaned_df = clean_market_data(raw_rows)
        print("\n--- Cleaned NEPSE Market Data ---")
        print(cleaned_df.head(10))
        print(f"\nTotal active tickers processed: {len(cleaned_df)}")
        
