from pydantic import Field

from .base import TradeXRocketObject


class RateCryptoCryptoDto(TradeXRocketObject):
    base_currency: str = Field(alias="baseCurrency")
    """From crypto currency"""
    quote_currency: str = Field(alias="quoteCurrency")
    """To crypto currency"""
    rate: int | float
    """Crypto rate in crypto"""
