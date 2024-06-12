# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# ファイルをコピー
COPY . .

# 非特権ユーザーを作成
RUN useradd -m myuser
USER myuser

RUN pip install --upgrade pip

# 必要なパッケージをインストール
RUN pip install --no-cache-dir Flask gunicorn

RUN export PATH="/home/myuser/.local/bin:$PATH"

# アプリを起動
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
