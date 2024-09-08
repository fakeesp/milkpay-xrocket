from pydantic import Field

from .app_balance import AppBalance
from .base import PayXRocketObject


class App(PayXRocketObject):
    name: str
    """Name of current app"""
    fee_percents: int | float = Field(alias="feePercents")
    """Fee for incoming transactions"""
    balances: list[AppBalance]
