# Pythonベースイメージ
FROM python:3.9-slim

# 作業ディレクトリ
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Flaskアプリを起動
CMD ["python", "app.py"]
