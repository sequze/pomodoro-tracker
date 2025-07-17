from datetime import datetime, timezone

from sqlalchemy.orm import mapped_column, Mapped


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now())