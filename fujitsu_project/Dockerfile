# ベースイメージを指定
FROM python:3.9-slim

# ポートの公開
EXPOSE 8080

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# pipのアップグレード
RUN pip install --upgrade pip

# コピー元のパスを変更
COPY . .

# 依存パッケージをインストール
RUN pip install --no-cache-dir Flask gunicorn

# アプリを起動
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
