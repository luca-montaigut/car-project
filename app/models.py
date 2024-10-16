from pydantic import BaseModel


class CarRequest(BaseModel):
    model: str
    color: str
