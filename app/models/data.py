from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    """Shared properties"""

    message: str = None
    source_name: Optional[str] = None


# noinspection PyUnusedName
class Item(ItemBase):
    """Properties to return to client"""

    status: str = None
    error: Optional[str] = None


class ItemInParse(ItemBase):
    pass
