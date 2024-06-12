# ベースイメージを指定
FROM python:3.9-slim

EXPOSE 8080

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# パスを設定
ENV PATH="/home/myuser/.local/bin:${PATH}"

# ファイルをコピー
COPY . .

# 依存パッケージをインストール
RUN pip install --no-cache-dir Flask gunicorn

# アプリを起動
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8080"]
