from pydantic import Field

from .base import TradeXRocketObject


class RateCryptoFiatDto(TradeXRocketObject):
    crypto_currency: str = Field(alias="cryptoCurrency")
    """Crypto currency"""
    fiat_currency: str = Field(alias="fiatCurrency")
    """Fiat currency"""
    rate: int | float
    """Crypto rate in fiat"""
