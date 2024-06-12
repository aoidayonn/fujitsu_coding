# ベースイメージを指定
FROM python:3.9-slim

EXPOSE 8080

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# 非特権ユーザーを作成
RUN useradd -m myuser
USER myuser

# 仮想環境を作成
RUN python3 -m venv /app/venv

# 仮想環境をアクティベート
RUN /bin/bash -c "source /app/venv/bin/activate"

# パスを設定
ENV PATH="/app/venv/bin:${PATH}"

# ファイルをコピー
COPY . .

# 依存パッケージをインストール
RUN pip install --no-cache-dir Flask gunicorn

# アプリを起動
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
