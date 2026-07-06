import pandas as pd
from database import SessionLocal
from models import DailyMarketInsights
from database import Base, engine


def load_data_to_db(df: pd.DataFrame):
    """
    Takes a cleaned Pandas DataFrame and saves its records permanently in to the SQLite database.
    """
    if df.empty:
        print("⚠ DataFrame is empty. Skipping database load.")
        return
    
    # Line 1 : Spin up an isloated transaction session from our factory
    db=SessionLocal()
    
    try:
        print(f"📥 Preparing to load {len(df)} records into the database...")
        
        #2 Optional Clean_up
        # This deletes previous runs so our data stays perfectly clean while testing.
        
        # Line 3: Loop through the DataFrame row by row
        # index is the row number, row contains the actual series data
        for index, row in df.iterrows():
            # Line 4 : Instantiate an ORM model record for each row
            record= DailyMarketInsights(
                symbol = str(row["Symbol"]), 
                ltp= float(row["LTP"]),
                diff_percent= float(row["Diff %"]),
                open_price= float(row["Open"]) if pd.notnull(row["Open"]) else None,
                high=float(row["High"]) if pd.notnull(row["High"]) else None,
                low=float(row["Low"]) if pd.notnull(row["Low"]) else None,
                turnover=float(row["Turnover"]) if pd.notnull(row["Turnover"]) else None,
            )
        
           # Line 5 : Adding the record to our staging queue
            db.add(record)
        
        # Line 6: Committing the entire queue to the local disk file in one go
        db.commit()
        print("🎉 Database sync complete! All records securely stored.")
        
    except Exception as e:
        # Line & Safesty net! Rollback changes if a crash happens midway
        db.rollback()
        print(f"❌ Error occurred while loading data: {e}")
    finally:
        # Line 8 : Closing  the database session to free up system memory
        db.close()

if __name__=="__main__":
    # Test script block to run the whole pipeline end-to-end
    from extractor import fetch_raw_table_rows
    from transformer import clean_market_data
    url = "https://www.sharesansar.com/today-share-price"
    print("🚀 Running full pipeline test from Scraper to DB Storage...")
    
    # 🛠️ FORCE TABLE GENERATION ONCE RIGHT HERE BEFORE INSERTING ROWS
    print("Ensuring structural tables exist...")
    Base.metadata.create_all(bind=engine)
    
    raw_rows= fetch_raw_table_rows(url)
    if raw_rows:
        cleaned_df=clean_market_data(raw_rows)
        load_data_to_db(cleaned_df)
