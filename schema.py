from typing import Optional, Text

from pydantic import BaseModel, EmailStr, Field


class VPABase(BaseModel):
    pg_merchant_id: str = Field(..., max_length=16, description="Merchant ID")
    #merchant_ref_no: str = Field(..., max_length=30, description="Unique order reference sent by merchant")
    payer_virtual_address: str = Field(..., max_length=255, description="Payer Virtual Address")
    status: str = Field(..., max_length=2, description="Transaction Status (T)")


    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "pg_merchant_id": "HDFC000008263034",
                "payer_virtual_address": "xpayback@hdfcbank",
                "status": "T"
            },
        }
