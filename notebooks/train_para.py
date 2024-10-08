from pydantic import BaseModel
class params(BaseModel):
    CountryCode_x:float
    Amount:float
    Value: float
    PricingStrategy:float
    hour:int
    day:int
    month:int
    year:int
    CountryCode_y: float
    hour_woe: float
    ProviderId_woe:float
    Value_woe:float
    PricingStrategy_woe: float
    ProductId_woe: float
    month_woe:float
    year_woe: float
    ProductCategory_woe: float
    Amount_woe: float
    day_woe: float
    ChannelId_woe: float