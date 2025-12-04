# schemas.py
from pydantic import BaseModel, ConfigDict

class Campaign(BaseModel):
    id: int
    name: str
    status: str
    clicks: int
    cost: float
    impressions: int

    # Allow reading from SQLAlchemy model attributes
    model_config = ConfigDict(from_attributes=True)
