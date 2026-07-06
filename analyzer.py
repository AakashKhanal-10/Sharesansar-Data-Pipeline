import pandas as pd
from transformer import clean_market_data

def generate_market_insights(df):
    if df.empty:
        print("No data available to analyze")
        return
    print("\n"+ "="*40)
    print("         DAILY MARKET INSIGHTS         ")
    print("="*40)
    # 🔍 Temporary Debug Line: Let's see the exact column names
    print("Available columns in your data are:", df.columns.tolist())
    
    #1 Calculate Top 5 Gainers
    print("\n📈 TOP 5 GAINERS:")
    gainers= df.sort_values(by='Diff %', ascending=False).head(5)
    print(gainers[["Symbol", "Diff %", "LTP"]].to_string(index=False))
    
    # 2. Calculate Top 5 Losers
    print("\n📉 TOP 5 LOSERS:")
    losers = df.sort_values(by='Diff %', ascending=True).head(5)
    print(losers[['Symbol', 'LTP', 'Diff %']].to_string(index=False))
    
    # 3. Calculate Liquidity Leaders(Highest Volume)
    if "Vol"in df.columns:
        print("\n💧 TOP 5 BY TRADING VOLUME:")
        volume_leaders=df.sort_values(by='Vol', ascending=False).head(5)
        print(volume_leaders[['Symbol', 'LTP', 'Vol']].to_string(index=False))
    
    #4. Average Market Price
    if "LTP" in df.columns:
        avg_price=df["LTP"].mean()
        print("\n📊 AVERAGE MARKET PRICE:")
        print(f"Rs. {avg_price:.2f}")
        
    #5. Highest Priced Stock
    if "LTP" in df.columns:
        highest=df.loc[df["LTP"].idxmax()]
        print("\n🏆 HIGHEST PRICED STOCK:")
        print(f"{highest['Symbol']}: Rs. {highest['LTP']}")

    #6. Lowest Priced Stock
    if "LTP"in df.columns:
        lowest=df.loc[df["LTP"].idxmin()]
        print("\n🥉 LOWEST PRICED STOCK:")
        print(f"{lowest['Symbol']}: Rs. {lowest['LTP']}")
        
    #7. Total Market Volume
    if "Vol" in df.columns:
        total_volume=df['Vol'].sum()
        print("\n📦 TOTAL MARKET VOLUME:") 
        print(f"{total_volume:,}")
        
if __name__=="__main__":
    from extractor import fetch_raw_table_rows
    
    url = "https://www.sharesansar.com/today-share-price"
    print("Fetching Live data for analysis..")
    raw_rows = fetch_raw_table_rows(url)
    
    if raw_rows:
        cleaned_df=clean_market_data(raw_rows)
        generate_market_insights(cleaned_df)
    
       
