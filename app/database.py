import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#  os.getenvはOSから環境変数を取得　学習用環境のため、第二引数のデフォルトURLを利用
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://customer_user:local_password@db:5432/customer_db",
)

#  データベースとの接続先窓口(engine)を作成
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  