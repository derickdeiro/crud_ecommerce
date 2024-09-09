from pydantic import BaseModel, PositiveFloat, EmailStr
from enum import Enum
from datetime import datetime as dt
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    supplier_email: EmailStr
    
    
class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: dt
    
    class Config:
        from_attributes = True
        
        
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    supplier_email: Optional[EmailStr] = None