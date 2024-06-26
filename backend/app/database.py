# データベース接続を管理するためのファイルを作成

import os  # OSモジュールをインポート
from sqlalchemy import create_engine  # SQLAlchemyのエンジンをインポート
from sqlalchemy.ext.declarative import declarative_base  # 基本クラスをインポート
from sqlalchemy.orm import sessionmaker  # セッションメーカーをインポート
from dotenv import load_dotenv  # dotenvからload_dotenvをインポート

# .envファイルを読み込む
load_dotenv()

# 環境変数からデータベース接続情報を取得
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# データベース接続のURLを正しい形式で設定
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# データベースエンジンの作成
engine = create_engine(DATABASE_URL)
# セッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 基本クラスの作成
Base = declarative_base()

# データベースセッションを取得する関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
