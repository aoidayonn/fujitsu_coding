# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# ファイルをコピー
COPY . .

RUN pip install --upgrade pip

# 必要なパッケージをインストール
RUN pip install --no-cache-dir Flask gunicorn

# アプリを起動
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
