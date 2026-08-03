# Python3.11入りの公式イメージをベースにする
FROM python:3.11-bookworm 

# コンテナ内の作業ディレクトリを/appに設定
WORKDIR /app

# 必要なライブラリ情報をコピー（コピー先は作業ディレクトリの/app）
COPY requirements.txt .

#　ライブラリを一括インストール
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトフォルダ内の全体をコンテナへコピー
COPY . .

# FastApi(uvicorn)を起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]  

