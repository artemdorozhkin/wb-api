from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class RealizationReport(BaseModel):
    """
    Модель для представления отчета о реализации.

    Attributes:
        realizationreport_id (int): Номер отчёта.
        date_from (datetime): Дата начала отчётного периода.
        date_to (datetime): Дата конца отчётного периода.
        create_dt (datetime): Дата формирования отчёта.
        currency_name (str): Валюта отчёта.
        suppliercontract_code (Optional[dict]): Договор.
        rrd_id (int): Номер строки.
        gi_id (int): Номер поставки.
        subject_name (str): Предмет.
        nm_id (int): Артикул WB.
        brand_name (str): Бренд.
        sa_name (str): Артикул продавца.
        ts_name (str): Размер.
        barcode (str): Баркод.
        doc_type_name (str): Тип документа.
        quantity (int): Количество.
        retail_price (float): Цена розничная.
        retail_amount (float): Сумма продаж (возвратов).
        sale_percent (int): Согласованная скидка.
        commission_percent (float): Процент комиссии.
        office_name (str): Склад.
        supplier_oper_name (str): Обоснование для оплаты.
        order_dt (datetime): Дата заказа.
        sale_dt (datetime): Дата продажи.
        rr_dt (datetime): Дата операции.
        shk_id (int): Штрих-код.
        retail_price_withdisc_rub (float): Цена розничная с учетом согласованной скидки.
        delivery_amount (int): Количество доставок.
        return_amount (int): Количество возвратов.
        delivery_rub (float): Стоимость логистики.
        gi_box_type_name (str): Тип коробов.
        product_discount_for_report (float): Согласованный продуктовый дисконт.
        supplier_promo (float): Промокод.
        rid (int): Уникальный идентификатор заказа.
        ppvz_spp_prc (float): Скидка постоянного покупателя.
        ppvz_kvw_prc_base (float): Размер кВВ без НДС, % базовый.
        ppvz_kvw_prc (float): Итоговый кВВ без НДС, %.
        sup_rating_prc_up (float): Размер снижения кВВ из-за рейтинга.
        is_kgvp_v2 (float): Размер снижения кВВ из-за акции.
        ppvz_sales_commission (float): Вознаграждение с продаж до вычета услуг поверенного, без НДС.
        ppvz_for_pay (float): К перечислению продавцу за реализованный товар.
        ppvz_reward (float): Возмещение за выдачу и возврат товаров на ПВЗ.
        acquiring_fee (float): Возмещение издержек по эквайрингу.
        acquiring_bank (str): Наименование банка-эквайера.
        ppvz_vw (float): Вознаграждение WB без НДС.
        ppvz_vw_nds (float): НДС с вознаграждения WB.
        ppvz_office_id (int): Номер офиса.
        ppvz_office_name (str): Наименование офиса доставки.
        ppvz_supplier_id (int): Номер партнера.
        ppvz_supplier_name (str): Партнер.
        ppvz_inn (str): ИНН партнера.
        declaration_number (str): Номер таможенной декларации.
        bonus_type_name (Optional[str]): Обоснование штрафов и доплат. Поле будет в ответе при наличии значения.
        sticker_id (Optional[str]): Цифровое значение стикера, который клеится на товар в процессе сборки заказа по схеме "Маркетплейс".
        site_country (str): Страна продажи.
        penalty (float): Штрафы.
        additional_payment (float): Доплаты.
        rebill_logistic_cost (Optional[float]): Возмещение издержек по перевозке. Поле будет в ответе при наличии значения.
        rebill_logistic_org (Optional[str]): Организатор перевозки. Поле будет в ответе при наличии значения.
        kiz (Optional[str]): Код маркировки. Поле будет в ответе при наличии значения.
        storage_fee (float): Стоимость хранения.
        deduction (float): Прочие удержания/выплаты.
        acceptance (float): Стоимость платной приёмки.
        srid (str): Уникальный идентификатор заказа.
        report_type (int): Тип отчёта. 1 — стандартный, 2 — для уведомления о выкупе.
    """

    realizationreport_id: int = Field(
        ..., alias="realizationreport_id", description="Номер отчёта."
    )
    date_from: datetime = Field(
        ..., alias="date_from", description="Дата начала отчётного периода."
    )
    date_to: datetime = Field(
        ..., alias="date_to", description="Дата конца отчётного периода."
    )
    create_dt: datetime = Field(
        ..., alias="create_dt", description="Дата формирования отчёта."
    )
    currency_name: Optional[str] = Field(
        None, alias="currency_name", description="Валюта отчёта."
    )
    suppliercontract_code: Optional[dict] = Field(
        None, alias="suppliercontract_code", description="Договор."
    )
    rrd_id: int = Field(..., alias="rrd_id", description="Номер строки.")
    gi_id: int = Field(..., alias="gi_id", description="Номер поставки.")
    subject_name: str = Field(..., alias="subject_name", description="Предмет.")
    nm_id: int = Field(..., alias="nm_id", description="Артикул WB.")
    brand_name: str = Field(..., alias="brand_name", description="Бренд.")
    sa_name: str = Field(..., alias="sa_name", description="Артикул продавца.")
    ts_name: str = Field(..., alias="ts_name", description="Размер.")
    barcode: str = Field(..., alias="barcode", description="Баркод.")
    doc_type_name: str = Field(..., alias="doc_type_name", description="Тип документа.")
    quantity: int = Field(..., alias="quantity", description="Количество.")
    retail_price: float = Field(
        ..., alias="retail_price", description="Цена розничная."
    )
    retail_amount: float = Field(
        ..., alias="retail_amount", description="Сумма продаж (возвратов)."
    )
    sale_percent: int = Field(
        ..., alias="sale_percent", description="Согласованная скидка."
    )
    commission_percent: float = Field(
        ..., alias="commission_percent", description="Процент комиссии."
    )
    office_name: str = Field(..., alias="office_name", description="Склад.")
    supplier_oper_name: str = Field(
        ..., alias="supplier_oper_name", description="Обоснование для оплаты."
    )
    order_dt: datetime = Field(
        ...,
        alias="order_dt",
        description="Дата заказа. Присылается с явным указанием часового пояса.",
    )
    sale_dt: datetime = Field(
        ...,
        alias="sale_dt",
        description="Дата продажи. Присылается с явным указанием часового пояса.",
    )
    rr_dt: datetime = Field(
        ...,
        alias="rr_dt",
        description="Дата операции. Присылается с явным указанием часового пояса.",
    )
    shk_id: int = Field(..., alias="shk_id", description="Штрих-код.")
    retail_price_withdisc_rub: float = Field(
        ...,
        alias="retail_price_withdisc_rub",
        description="Цена розничная с учетом согласованной скидки.",
    )
    delivery_amount: int = Field(
        ..., alias="delivery_amount", description="Количество доставок."
    )
    return_amount: int = Field(
        ..., alias="return_amount", description="Количество возвратов."
    )
    delivery_rub: float = Field(
        ..., alias="delivery_rub", description="Стоимость логистики."
    )
    gi_box_type_name: str = Field(
        ..., alias="gi_box_type_name", description="Тип коробов."
    )
    product_discount_for_report: float = Field(
        ...,
        alias="product_discount_for_report",
        description="Согласованный продуктовый дисконт.",
    )
    supplier_promo: float = Field(..., alias="supplier_promo", description="Промокод.")
    rid: int = Field(..., alias="rid", description="Уникальный идентификатор заказа.")
    ppvz_spp_prc: float = Field(
        ..., alias="ppvz_spp_prc", description="Скидка постоянного покупателя."
    )
    ppvz_kvw_prc_base: float = Field(
        ..., alias="ppvz_kvw_prc_base", description="Размер кВВ без НДС, % базовый."
    )
    ppvz_kvw_prc: float = Field(
        ..., alias="ppvz_kvw_prc", description="Итоговый кВВ без НДС, %."
    )
    sup_rating_prc_up: float = Field(
        ...,
        alias="sup_rating_prc_up",
        description="Размер снижения кВВ из-за рейтинга.",
    )
    is_kgvp_v2: float = Field(
        ..., alias="is_kgvp_v2", description="Размер снижения кВВ из-за акции."
    )
    ppvz_sales_commission: float = Field(
        ...,
        alias="ppvz_sales_commission",
        description="Вознаграждение с продаж до вычета услуг поверенного, без НДС.",
    )
    ppvz_for_pay: float = Field(
        ...,
        alias="ppvz_for_pay",
        description="К перечислению продавцу за реализованный товар.",
    )
    ppvz_reward: float = Field(
        ...,
        alias="ppvz_reward",
        description="Возмещение за выдачу и возврат товаров на ПВЗ.",
    )
    acquiring_fee: float = Field(
        ..., alias="acquiring_fee", description="Возмещение издержек по эквайрингу."
    )
    acquiring_bank: str = Field(
        ..., alias="acquiring_bank", description="Наименование банка-эквайера."
    )
    ppvz_vw: float = Field(
        ..., alias="ppvz_vw", description="Вознаграждение WB без НДС."
    )
    ppvz_vw_nds: float = Field(
        ..., alias="ppvz_vw_nds", description="НДС с вознаграждения WB."
    )
    ppvz_office_id: int = Field(..., alias="ppvz_office_id", description="Номер офиса.")
    ppvz_office_name: str = Field(
        ..., alias="ppvz_office_name", description="Наименование офиса доставки."
    )
    ppvz_supplier_id: int = Field(
        ..., alias="ppvz_supplier_id", description="Номер партнера."
    )
    ppvz_supplier_name: str = Field(
        ..., alias="ppvz_supplier_name", description="Партнер."
    )
    ppvz_inn: str = Field(..., alias="ppvz_inn", description="ИНН партнера.")
    declaration_number: str = Field(
        ..., alias="declaration_number", description="Номер таможенной декларации."
    )
    bonus_type_name: Optional[str] = Field(
        None,
        alias="bonus_type_name",
        description="Обоснование штрафов и доплат. Поле будет в ответе при наличии значения.",
    )
    sticker_id: Optional[str] = Field(
        None,
        alias="sticker_id",
        description="Цифровое значение стикера, который клеится на товар в процессе сборки заказа по схеме 'Маркетплейс'.",
    )
    site_country: str = Field(..., alias="site_country", description="Страна продажи.")
    penalty: float = Field(..., alias="penalty", description="Штрафы.")
    additional_payment: float = Field(
        ..., alias="additional_payment", description="Доплаты."
    )
    rebill_logistic_cost: Optional[float] = Field(
        None,
        alias="rebill_logistic_cost",
        description="Возмещение издержек по перевозке. Поле будет в ответе при наличии значения.",
    )
    rebill_logistic_org: Optional[str] = Field(
        None,
        alias="rebill_logistic_org",
        description="Организатор перевозки. Поле будет в ответе при наличии значения.",
    )
    kiz: Optional[str] = Field(
        None,
        alias="kiz",
        description="Код маркировки. Поле будет в ответе при наличии значения.",
    )
    storage_fee: Optional[float] = Field(
        None, alias="storage_fee", description="Стоимость хранения."
    )
    deduction: Optional[float] = Field(
        None, alias="deduction", description="Прочие удержания/выплаты."
    )
    acceptance: Optional[float] = Field(
        None, alias="acceptance", description="Стоимость платной приёмки."
    )
    srid: str = Field(
        ...,
        alias="srid",
        description="Уникальный идентификатор заказа. Примечание для использующих API Marketplace: srid равен rid в ответах методов сборочных заданий.",
    )
    report_type: Optional[int] = Field(
        None,
        alias="report_type",
        description="Тип отчёта. 1 — стандартный, 2 — для уведомления о выкупе.",
    )

    class Config:
        populate_by_name = True


class RealizationReports(BaseModel):
    realization_reports: List[RealizationReport]
