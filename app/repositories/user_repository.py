from sqlalchemy import update, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.schemas.user import UserCreateSchema, UserUpdateSchema

class UserNotFoundError(Exception):
    """User not found"""
    pass


class UserRepository:
    async def create(self,
                     session: AsyncSession,
                     data: UserCreateSchema) -> User:
        u = User(
            email=data.email,
            password_hash=data.password, #TODO: хеширование пароля
            full_name=data.full_name,
            role=data.role,
        )
        session.add(u)
        await session.commit()
        await session.refresh(u)
        return u

    async def update(
            self,
            session: AsyncSession,
            data: UserUpdateSchema,
            id: int) -> User:
        u = await session.get(User, id)
        if u is None:
            raise UserNotFoundError
        for name, value in data.model_dump(exclude_unset=True).items():
            setattr(u, name, value)
        await session.commit()
        await session.refresh(u)
        return u

    async def delete_by_id(
            self,
            session: AsyncSession,
            id: int):
        await session.execute(delete(User).where(User.id == id))
        await session.commit()

    async def get_by_id(self,
                        session: AsyncSession,
                        id: int) -> User:
        u = await session.get(User, id)
        return u

    # async def get_multi(
    #         self,
    #         order: str = "id",
    #         limit: int = 100,
    #         offset:int = 0,
    #         **filters,
    # ) -> list[ModelType]:
    #     async with self.session_factory() as session:
    #         stmt = select(self.model).order_by(*order).filter_by(**filters).limit(limit).offset(offset)
    #         row = await session.execute(stmt)
    #         return row.scalars().all()