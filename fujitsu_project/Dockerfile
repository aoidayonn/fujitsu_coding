# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# ファイルをコピー
COPY . .

# 必要なパッケージをインストール
RUN pip install --no-cache-dir Flask

# アプリを起動
CMD ["python", "app.py"]
