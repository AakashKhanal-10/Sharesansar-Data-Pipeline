from pydantic import BaseModel
from datetime import datetime

# 1 Base Class sharing data configuration attributes
class MarketInsightsResponse(BaseModel):
    id:int
    symbol:str
    ltp:float
    diff_percent: float
    open_price: float | None
    high: float | None
    low: float | None
    volume:float | None
    turnover: float | None
    fetched_at: datetime
    
    
    # 2 Tell Pydantic to read ORM objects directly
    model_config = {
        "from_attributes": True
    }