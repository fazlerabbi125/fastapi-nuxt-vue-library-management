# from typing import List, Optional
from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy_utils import EmailType, Timestamp, generic_repr
from enum import Enum

class UserRoles(Enum):
    ADMIN = "admin"
    USER = "user"

@generic_repr
class User(Base, Timestamp):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(EmailType, unique=True)
    password: Mapped[str | None] = mapped_column(sa.String(255))
    active: Mapped[bool] = mapped_column(default=True, nullable=False)
    role: Mapped[str] = mapped_column(
        # ChoiceType from sqlalchemy_utils not used as migration adds extra length argument
        sa.Enum(UserRoles),
        default=UserRoles.USER.value,
        nullable=False,
    )
