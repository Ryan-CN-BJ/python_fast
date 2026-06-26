# model/main.py
import asyncio
from sqlalchemy import text, select
from app.model.base import Base
from app.model.category import Category
from app.model.product import Product
from app.model.sku import Sku

from app.core.db import get_engine, get_sesstion_factory

session_factory = get_sesstion_factory()


async def init_db():
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("✅ 数据库表创建完成")


async def orm_insert():
    """直接用 SQL 字符串插入数据"""
    async with session_factory.begin() as session:
        product = Product(
            name="iPhone 16",
            description="最新款智能手机",
            brand="Apple",
        )
        session.add(product)
        product2 = Product(
            name="iPhone 15",
            description="上一代旗舰",
            brand="Apple",
        )
        session.add(product2)
        category = Category(name="手机", description="移动通信设备")
        session.add(category)
    print("✅ 数据插入完成")


async def orm_search_product():
    async with session_factory() as session:
        stmt = select(Product).where(Product.name.like("%iPhone%"))
        result = await session.execute(stmt)
        # scalars() 返回模型实例，可直接访问属性
        products = result.scalars().all()
        for p in products:
            print(f"  [{p.id}] {p.name} - {p.brand}")
        print("✅ 数据查询完成")


async def orm_update():
    async with session_factory.begin() as session:
        stmt = select(Product).where(Product.id == 1)
        result = await session.execute(stmt)
        product = result.scalar_one()
        # 直接修改 Python 对象属性，session 提交时自动生成 UPDATE
        product.name = "iPhone 16 Pro"
    print("✅ ORM 更新完成")


async def orm_delete():
    async with session_factory.begin() as session:
        stmt = select(Product).where(Product.id == 2)
        result = await session.execute(stmt)
        product = result.scalar_one()
        await session.delete(product)
    print("✅ ORM 删除完成")


async def test_connection():
    engine = get_engine()
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            value = result.scalar()
            print(f"✅ 连接成功！查询结果: {value}")
    except Exception as e:
        print(f"❌ 连接失败: {e}")


async def main():
    await init_db()
    await orm_insert()
    await orm_search_product()
    await orm_update()
    await orm_delete()
    # await test_connection()


if __name__ == "__main__":
    asyncio.run(main())
