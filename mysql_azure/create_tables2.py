# カラム名と中身の商品10個入れるコード
# import osとmysql.connectorのモジュールをインポート

import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# .envファイルから環境変数を取得
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
SSL_CERT_PATH = os.getenv("SSL_CERT_PATH")

# SSL証明書の絶対パスを取得
base_path = os.path.dirname(os.path.abspath(__file__))
ssl_cert_path = os.path.join(base_path, SSL_CERT_PATH)

# 接続文字列情報を設定
config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_NAME,
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': ssl_cert_path
}

# 接続文字列を構築して接続
try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("Error:", err)
else:
    cursor = conn.cursor()
    print("Cursor created")

    # 既存のテーブルがあれば削除
    cursor.execute("DROP TABLE IF EXISTS transaction_details;")
    cursor.execute("DROP TABLE IF EXISTS transactions;")
    cursor.execute("DROP TABLE IF EXISTS products;")
    print("Finished dropping tables (if existed).")

    # productsテーブルの作成
    cursor.execute("""
        CREATE TABLE products (
            prd_id INT AUTO_INCREMENT PRIMARY KEY,
            code CHAR(13) NOT NULL UNIQUE,
            name VARCHAR(50) NOT NULL,
            price INT NOT NULL
        );
    """)
    print("Finished creating products table.")

    # transactionsテーブルの作成
    cursor.execute("""
        CREATE TABLE transactions (
            trd_id INT AUTO_INCREMENT PRIMARY KEY,
            datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            emp_cd CHAR(10) DEFAULT '9999999999',
            store_cd CHAR(5) DEFAULT '30',
            pos_no CHAR(3) DEFAULT '90',
            total_amt INT NOT NULL
        );
    """)
    print("Finished creating transactions table.")

    # transaction_detailsテーブルの作成
    cursor.execute("""
        CREATE TABLE transaction_details (
            dtl_id INT AUTO_INCREMENT PRIMARY KEY,
            trd_id INT,
            prd_id INT,
            prd_code CHAR(13),
            prd_name VARCHAR(50),
            prd_price INT,
            FOREIGN KEY (trd_id) REFERENCES transactions(trd_id),
            FOREIGN KEY (prd_id) REFERENCES products(prd_id)
        );
    """)
    print("Finished creating transaction_details table.")

    # 商品データの挿入
    products = [
        ('4900000000010', 'apple', 100),
        ('4900000000027', 'banana', 150),
        ('4900000000034', 'orange', 120),
        ('4900000000041', 'bread', 200),
        ('4900000000058', 'milk', 180),
        ('4900000000065', 'rice', 300),
        ('4900000000072', 'toothpaste', 250),
        ('4900000000089', 'shampoo', 500),
        ('4900000000096', 'soap', 80),
        ('4900000000102', 'chocolate', 220)
    ]

    for code, name, price in products:
        cursor.execute("""
            INSERT INTO products (code, name, price)
            VALUES (%s, %s, %s)
        """, (code, name, price))

    print("Finished inserting products data.")

    # 変更のコミット
    conn.commit()
    cursor.close()
    conn.close()
    print("Done.")
