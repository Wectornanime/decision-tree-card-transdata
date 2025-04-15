from pydantic import BaseModel

class PredictJsonModel(BaseModel):
    ratio_to_median_purchase_price: float
    online_order: int
    distance_from_home: float
    distance_from_last_transaction: float
