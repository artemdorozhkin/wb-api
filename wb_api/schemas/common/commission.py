from typing import List

from pydantic import BaseModel, Field


class Commission(BaseModel):
    """
    Модель комиссии по категориям товаров.

    Attributes:
        kgvp_marketplace (float): Комиссия по модели Склад продавца — везу на склад WB, %
        kgvp_supplier (float): Комиссия по моделям Склад продавца — везу самостоятельно до клиента и Склад продавца — Курьером WB, %
        kgvp_supplier_express (float): Комиссия по модели Склад продавца — везу самостоятельно до клиента экспресс, %
        paid_storage_kgvp (float): Комиссия по модели Склад WB, %
        parent_ID (int): ID родительской категории
        parent_name (str): Название родительской категории
        subject_ID (int): ID предмета
        subject_name (str): Название предмета
    """

    kgvp_marketplace: float = Field(
        ...,
        alias="kgvpMarketplace",
        description="Комиссия по модели Склад продавца — везу на склад WB, %",
    )
    kgvp_supplier: float = Field(
        ...,
        alias="kgvpSupplier",
        description="Комиссия по моделям Склад продавца — везу самостоятельно до клиента и Склад продавца — Курьером WB, %",
    )
    kgvp_supplier_express: float = Field(
        ...,
        alias="kgvpSupplierExpress",
        description="Комиссия по модели Склад продавца — везу самостоятельно до клиента экспресс, %",
    )
    paid_storage_kgvp: float = Field(
        ..., alias="paidStorageKgvp", description="Комиссия по модели Склад WB, %"
    )
    parent_ID: int = Field(
        ..., alias="parentID", description="ID родительской категории"
    )
    parent_name: str = Field(
        ..., alias="parentName", description="Название родительской категории"
    )
    subject_ID: int = Field(..., alias="subjectID", description="ID предмета")
    subject_name: str = Field(..., alias="subjectName", description="Название предмета")

    class Config:
        populate_by_name = True


class Commissions(BaseModel):
    commissions: List[Commission]
