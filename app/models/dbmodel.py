from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime] = Field(alias="createdAt")
    updated_at: Optional[datetime] = Field(alias="updatedAt")


class DBModelMixin(DateTimeModelMixin):
    id: Optional[int] = None
