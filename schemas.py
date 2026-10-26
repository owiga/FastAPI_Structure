from pydantic import BaseModel, HttpUrl, Field


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


class Url(BaseModel):
    url: HttpUrl
    price: str
    check_interval: int
