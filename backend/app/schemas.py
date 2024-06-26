# データのバリデーションとシリアライゼーションのためにPydanticスキーマを定義
# スキーマ定義では、データが正しい形式であるかをチェックし、データを送受信するために使いやすい形式に変換するための設定を行う
# Pydanticというライブラリを使って実施
# app/schemas.py

from pydantic import BaseModel  # PydanticのBaseModelをインポート

# 商品作成用のスキーマを定義
class ProductCreate(BaseModel):
    code: str  # 商品コード

# 商品読み取り用のスキーマを定義
class Product(BaseModel):
    prd_id: int  # 商品ID
    code: str  # 商品コード
    name: str  # 商品名
    price: int  # 商品価格

    # モデル設定を定義
    class Config:
        from_attributes = True  # 属性からの変換を許可
