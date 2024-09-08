from typing import Optional

from pydantic import Field
from stollen.enums import HTTPMethod

from ..types import WithdrawalDto
from .base import PayXRocketMethod


class Withdrawal(
    PayXRocketMethod[WithdrawalDto],
    http_method=HTTPMethod.POST,
    api_method="/app/withdrawal",
    returning=WithdrawalDto,
    response_data_key=["data"],
):
    """
    Make withdrawal of funds to external wallet
    """

    network: str
    """Network code"""
    address: str
    """Withdrawal address"""
    currency: str
    """Currency code"""
    amount: int | float
    """Withdrawal amount. 9 decimal places, others cut off"""
    withdrawal_id: str = Field(serialization_alias="withdrawalId")
    """Unique withdrawal ID in your system to prevent double spends"""
    comment: Optional[str] = None
    """Withdrawal comment"""