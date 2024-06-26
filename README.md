# Tech0_STEP4_pos.app
# Next.js (frontend)
1. フロントエンドのディレクトリ作成(Next.jsのパッケージインストール)
    npx create-next-app@latest frontend --ts
    ※y/nの選択は<terminal.png>を参照
    ※"frontend"はディレクトリ名なので任意の名前（が、frontendにしてるとわかりやすい）
2.  frontendのディレクトリに移動（ターミナル上）
    cd frontend
3. axiosの追加インストール（ブラウザとNode.jsの両方で使用できるHTTPクライアント）
    npm install axios
    ※https://qiita.com/Akihiro0711/items/fa22bfea27d686ed3430
    ※JavaScriptは言語の名前、Next.jsはフレームワークの名前（フレームワーク：pythonで言うとStreamlitやFlaskのようなもの）
    ※Next.jsの中にNode.jsがある（Node.jsとはサーバーサイド（バックエンド）でJavaScriptを実行するためのランタイム環境）

memo
    Next.jsとaxios
    なぜaxiosを使うのか？
        (1)簡単にデータを取りに行ける：
            axiosは、他のウェブサイトやAPIからデータを取ってくるための便利なツールです。ブラウザからリクエストを送って、レスポンスを簡単に受け取ることができます。
        (2)どこでも使える：
            axiosはブラウザとサーバー（Node.js）どちらでも使えるので、どちらの環境でも同じコードでデータを取ってこれます。

    Next.jsとNode.js
    どう関係しているのか？
        (1)Next.jsはNode.jsの上で動く：
            Next.jsはNode.jsという土台の上で動きます。Node.jsはJavaScriptをサーバー側で動かすためのものです。
        (2)サーバーサイドレンダリング（SSR）：
            Next.jsはサーバーでページを作ってからブラウザに送ることができます。これをSSRと言います。これにより、ページの表示が速くなり、検索エンジンにも優しいです。
        (3)APIルート：
            Next.jsではAPIを簡単に作れます。/pages/apiフォルダにファイルを置くだけで、そのファイルがAPIエンドポイントとして動きます。

    まとめ
        (1)Next.jsはウェブサイトやアプリを作るためのツールで、Node.jsの上で動きます。
        (2)axiosはデータを取ってくるためのツールで、Next.jsの中でも使えます。
        (3)Next.jsを使うと、ブラウザからデータを取ってきたり、サーバーでAPIを作ったりするのが簡単にできます。


# FastAPI（backend）
1. 仮想環境の作成
    conda create --name pos_app python=3.12
    ※"pos_app"は任意の名前
2. 仮想環境を起動
    conda activate pos_app
    ※"pos_app"は任意の仮想環境を指定
3. バックエンドのディレクトリ作成
    mkdir backend
    ※"backend"は任意の名前（が、backendにしてるとわかりやすい）
4. backendのディレクトリに移動（ターミナル上）
    cd backend
5. FastAPIのパッケージインストール
    pip install fastapi uvicorn mysql-connector-python pydantic
6. backendの中にディレクトリを作成（以下の構造で）
    backend/
    ├── app/
    │   ├── main.py
    │   ├── models.py
    │   ├── schemas.py
    │   └── database.py
    └── requirements.txt


# Azure MySQLへの接続
Azure portal にサインイン
https://portal.azure.com/#@admintech0jp.onmicrosoft.com/resource/subscriptions/9b680e6d-e5a6-4381-aad5-a30afcbc8459/resourceGroups/tech0-gen-7-step4-shared-rdb/providers/Microsoft.DBforMySQL/flexibleServers/tech0-db-step4-studentrdb-7/overview
ダッシュボードから、1班のデータサーバを選択
1班サーバーの [概要] ページから、 [サーバー名] と [サーバー管理者ログイン名] を記入。
    ※パスワードを忘れた場合も、このページからパスワードをリセットすることができる
[サーバー名] tech0-db-step4-studentrdb-1.mysql.database.azure.com
[サーバー管理者ログイン名] tech0gen7student
[データベータベース] pos_app_mi_rin
[ユーザー名]tech0gen7student
[パスワード]vY7JZNfU

データベース
    pos_app_mi_rin
    ※クイックスタート用に"techga0"データベースも作成した
ネットワーク
    ファイアウォール規則名 : mi_rin
        開始のIPアドレス : 192.168.11.10
        終了のIPアドレス : 192.168.11.10
    ファイアウォール規則名 : ClientIPAddress_2024-6-16_0-38-10
        開始のIPアドレス : 121.86.5.179
        終了のIPアドレス : 121.86.5.179
ターミナルで確認する
    ifconfig
        ※<en0>のIPアドレスを確認する

Microsoftのクイックスタートを見ながら接続をトライ
https://learn.microsoft.com/ja-jp/azure/mysql/single-server/connect-python
1. DigiCertGlobalRootG2 SSL 証明書をダウンロードして、createtable.py と同じディレクトリに保管
    以下のコードの箇所で証明書が稼働
        # Obtain the absolute path of the SSL certificate
        base_path = os.path.dirname(os.path.abspath(__file__))
        ssl_cert_path = os.path.join(base_path, 'DigiCertGlobalRootG2.crt.pem')
2. 今後自分の作成するアプリでもmysqlと接続するpythonと同じ階層にこの証明書を置いておく


# MySQL（DB = SQL）
1. mysqlのディレクトリを作成
2. mysqlとローカルを繋ぐためのpythonファイルを作成
    create_tables.py
    ※任意のファイル名
    ※前述でダウンローとした証明書「DigiCertGlobalRootG2」と同じ階層に作成すること
3. mysqlと接続
    python create_tables.py




# フロントエンドとバックエンドで.envファイルと.gitignoreファイルを分けるメリット
1. .envファイルを分けるメリット
    セキュリティの向上:
        フロントエンドとバックエンドでは、異なる環境変数を使用します。フロントエンドではAPIエンドポイントなど、公開しても問題ない情報を設定しますが、バックエンドではデータベースのパスワードなどの機密情報を設定します。
        分けることで、機密情報が誤ってフロントエンドに露出するリスクを減らせます。
    管理の簡素化:
        フロントエンドとバックエンドの環境変数を分けて管理することで、各プロジェクトで必要な設定を簡単に見つけて編集できます。
        例えば、APIエンドポイントを変更する場合はフロントエンドの.envファイルだけを編集すれば良いので、管理が楽になります。
    デプロイの容易化:
        フロントエンドとバックエンドがそれぞれ異なるサーバーにデプロイされる場合、それぞれのサーバーに適した環境変数を簡単に設定できます。
        分けることで、環境ごとの設定変更が容易になります。
2. .gitignoreファイルを分けるメリット
    プロジェクト構造の明確化:
        フロントエンドとバックエンドで異なるビルド成果物や依存ファイルが生成されます。これらを分けて管理することで、プロジェクト構造が明確になります。
        例えば、フロントエンドのビルド成果物は.next/ディレクトリに保存され、バックエンドのビルド成果物はdist/ディレクトリに保存されるため、それぞれの.gitignoreに適切なエントリを追加することで、どのファイルが無視されるべきかが明確になります。
    不要ファイルの混在防止:
        フロントエンドとバックエンドで無視すべきファイルが異なるため、分けることで不要なファイルの混在を防げます。
        例えば、フロントエンドのnode_modules/ディレクトリとバックエンドの__pycache__/ディレクトリを個別に管理できます。
    チーム開発の効率化:
        フロントエンドとバックエンドの開発者が異なる場合、それぞれが自分の作業に関連するファイルだけを管理しやすくなります。
        分けることで、各開発者が自分の担当部分に集中でき、効率的に開発を進められます。
