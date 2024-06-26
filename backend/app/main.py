# FastAPIのエンドポイントを定義
# app/main.py

from fastapi import FastAPI, Depends, HTTPException  # FastAPIの依存関係と例外処理をインポート
from fastapi.middleware.cors import CORSMiddleware  # CORSミドルウェアをインポート
from . import models, schemas  # アプリケーションのモデルとスキーマをインポート
from .database import engine, get_db  # データベースエンジンとセッション取得関数をインポート
from sqlalchemy.orm import Session  # SQLAlchemyのセッションをインポート

app = FastAPI()

# CORS設定を追加
origins = [
    "http://localhost:3000",  # フロントエンドからのリクエストを許可
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 許可されたオリジンを設定
    allow_credentials=True,  # 資格情報を許可
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのヘッダーを許可
)

@app.get("/products/")
def read_products(db: Session = Depends(get_db)):
    """
    すべての商品を取得するエンドポイント
    """
    products = db.query(models.Product).all()
    return products

@app.post("/products/")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    新しい商品を作成するエンドポイント
    """
    db_product = models.Product(code=product.code, name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/{code}")
def read_product_by_code(code: str, db: Session = Depends(get_db)):
    """
    商品コードに基づいて商品を取得するエンドポイント
    """
    product = db.query(models.Product).filter(models.Product.code == code).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
