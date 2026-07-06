from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, Integer, String, DateTime
from database import datetime,timezone
from database import Base


class DailyMarketInsights(Base):
    __tablename__= "daily_market_insights"
    
    # Column 1: The unique identifier
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    # Column 2: The  Timestamp of the data
    fetched_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Column 3+ : The Sharesansar Market Data Columns
    symbol: Mapped[str]= mapped_column(String,index=True, nullable=False)
    ltp: Mapped[float]= mapped_column(Float,nullable=False)
    diff_percent: Mapped[float]= mapped_column(Float,nullable=False)
    open_price: Mapped[float]= mapped_column(Float, nullable=False)
    high:Mapped[float]=mapped_column(Float, nullable=False)
    low: Mapped[float] = mapped_column(Float, nullable=True)
    volume: Mapped[float] = mapped_column(Float, nullable=True)
    turnover: Mapped[float] = mapped_column(Float, nullable=True)