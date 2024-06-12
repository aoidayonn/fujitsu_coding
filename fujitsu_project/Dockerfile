# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# 非特権ユーザーを作成
RUN useradd -m myuser
USER myuser

# パスを設定
ENV PATH="/home/myuser/.local/bin:${PATH}"

# ファイルをコピー
COPY . .

# 必要なパッケージをインストール
RUN pip install --no-cache-dir Flask gunicorn

# アプリを起動
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
