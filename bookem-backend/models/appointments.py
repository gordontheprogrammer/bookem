from pydantic import BaseModel
from datetime import datetime

class AppointmentIn(BaseModel):
    name: str
    date: datetime
    description: str
    price: int
