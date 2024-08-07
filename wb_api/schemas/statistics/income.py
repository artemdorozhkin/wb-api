from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class Income(BaseModel):
    """
    Модель для представления информации о поставке.

    Attributes:
        income_id (int): Номер поставки.
        number (str): Номер УПД. Максимальная длина - 40 символов.
        date (date): Дата поступления. Если часовой пояс не указан, то берется Московское время UTC+3.
        last_change_date (datetime): Дата и время обновления информации в сервисе.
                                     Это поле соответствует параметру dateFrom в запросе.
                                     Если часовой пояс не указан, то берется Московское время UTC+3.
        supplier_article (str): Артикул продавца. Максимальная длина - 75 символов.
        tech_size (str): Размер товара (пример S, M, L, XL, 42, 42-43). Максимальная длина - 30 символов.
        barcode (str): Бар-код. Максимальная длина - 30 символов.
        quantity (int): Количество.
        total_price (float): Цена из УПД.
        date_close (date): Дата принятия (закрытия) в WB. Если часовой пояс не указан, то берется Московское время UTC+3.
        warehouse_name (str): Название склада. Максимальная длина - 50 символов.
        nm_id (int): Артикул WB.
        status (str): Текущий статус поставки. Максимальная длина - 50 символов. Значение: "Принято".
    """

    income_id: int = Field(..., alias="incomeId", description="Номер поставки")
    number: str = Field(..., max_length=40, description="Номер УПД")
    date: datetime = Field(
        ...,
        description="Дата поступления. Если часовой пояс не указан, то берется Московское время UTC+3",
    )
    last_change_date: datetime = Field(
        ...,
        alias="lastChangeDate",
        description="Дата и время обновления информации в сервисе. Это поле соответствует параметру dateFrom в запросе. Если часовой пояс не указан, то берется Московское время UTC+3",
    )
    supplier_article: str = Field(
        ..., alias="supplierArticle", max_length=75, description="Артикул продавца"
    )
    tech_size: str = Field(
        ...,
        alias="techSize",
        max_length=30,
        description="Размер товара (пример S, M, L, XL, 42, 42-43)",
    )
    barcode: str = Field(..., max_length=30, description="Бар-код")
    quantity: int = Field(..., description="Количество")
    total_price: float = Field(..., alias="totalPrice", description="Цена из УПД")
    date_close: datetime = Field(
        ...,
        alias="dateClose",
        description="Дата принятия (закрытия) в WB. Если часовой пояс не указан, то берется Московское время UTC+3",
    )
    warehouse_name: str = Field(
        ..., alias="warehouseName", max_length=50, description="Название склада"
    )
    nm_id: int = Field(..., alias="nmId", description="Артикул WB")
    status: str = Field(
        ..., max_length=50, description='Текущий статус поставки. Значение: "Принято"'
    )

    class Config:
        populate_by_name = True


class Incomes(BaseModel):
    incomes: List[Income]
