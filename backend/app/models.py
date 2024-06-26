# データベースのモデル（テーブル）を定義
# app/models.py

from sqlalchemy import Column, Integer, String  # SQLAlchemyのカラムタイプをインポート
from .database import Base  # データベースの基本クラスをインポート

# 商品モデルを定義
class Product(Base):
    __tablename__ = "products"  # テーブル名を設定

    prd_id = Column(Integer, primary_key=True, index=True)  # 商品ID（プライマリキー）
    code = Column(String(13), unique=True, index=True)  # 商品コード（ユニーク、インデックス付き）
    name = Column(String(50))  # 商品名
    price = Column(Integer)  # 商品価格
