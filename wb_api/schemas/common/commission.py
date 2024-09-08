from typing import List

from pydantic import BaseModel, Field


class Commission(BaseModel):
    """
    Модель комиссии по категориям товаров.

    Attributes:
        kgvp_marketplace (float)
        kgvp_supplier (float)
        kgvp_supplier_express (float)
        paid_storage_kgvp (float)
        parent_ID (int)
        parent_name (str)
        subject_ID (int)
        subject_name (str)
    """

    kgvp_marketplace: float = Field(..., alias="kgvpMarketplace")
    kgvp_supplier: float = Field(..., alias="kgvpSupplier")
    kgvp_supplier_express: float = Field(..., alias="kgvpSupplierExpress")
    paid_storage_kgvp: float = Field(..., alias="paidStorageKgvp")
    parent_ID: int = Field(..., alias="parentID")
    parent_name: str = Field(..., alias="parentName")
    subject_ID: int = Field(..., alias="subjectID")
    subject_name: str = Field(..., alias="subjectName")

    class Config:
        populate_by_name = True


class Commissions(BaseModel):
    commissions: List[Commission]
