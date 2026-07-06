from fastapi import FastAPI ,Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

# Importing the unerlying database structures and schemas
from database import SessionLocal
from models import DailyMarketInsights
import schemas

#1 Initializing the FastAPI application
app= FastAPI(title="Nepal Share Market Live Analysis API")

#2 The Database Connection Session Lifecycle Dependency
def get_db():
    db=SessionLocal()
    try:
        yield db # Suspends executing while providing the connection to the route 
    finally:
        db.close() # Guarantees the database values closes safely when request terminates
            
# 3 Endpoint 1 : Fetched ALL scrapped stock market metrices
@app.get("/api/market",response_model=List[schemas.MarketInsightsResponse])  
def get_all_market_data(db:Session= Depends(get_db)):
    statement=select(DailyMarketInsights)
    result=db.scalars(statement).all()
    return result

# 4 Endpoin 2 : Fetch Top 5 Gainers dynamially
@app.get("/api/market/gainers",response_model=List[schemas.MarketInsightsResponse])
def get_top_gainers(db:Session=Depends(get_db)):
    statement=select(DailyMarketInsights).order_by(DailyMarketInsights.diff_percent.desc()).limit(5)
    return db.scalars(statement).all()

# 5. Endpoint 3: Fetch Top 5 Losers 
@app.get("/api/market/losers", response_model=List[schemas.MarketInsightsResponse])
def get_top_losers(db: Session = Depends(get_db)):
    statement = select(DailyMarketInsights).order_by(DailyMarketInsights.diff_percent.asc()).limit(5)
    return db.scalars(statement).all()


# 6. Endpoint 4: Search for a single specific stock identifier symbol
@app.get("/api/market/{symbol}",response_model=schemas.MarketInsightsResponse)
def get_stock_by_symbol(symbol:str, db: Session= Depends(get_db)):
    statement= select(DailyMarketInsights).where(DailyMarketInsights.symbol==symbol.upper())
    stock=db.scalar(statement)
    
    if not stock:
        raise HTTPException(status_code=404,details=f"Stock ticker symbol '{symbol} not found'")
    return stock