#!/bin/bash

# Configuration
HOST="173.209.32.66"
USER="fxgacz89"
REMOTE_DIR="public_html"
LOCAL_DIR="/Users/mayukookada/Desktop/DRPwebsite"
PORT=27 # Using port 27 as seen in deploy.sh

echo "=== $HOST へのデプロイを開始します (SFTP/SCP) ==="
echo "ローカルディレクトリ: $LOCAL_DIR"
echo "リモートディレクトリ: $REMOTE_DIR"

echo "接続中..."
echo "パスワードを求められたら、SFTPのパスワードを入力してください。"

# Upload files using SCP (Secure Copy, uses SSH/SFTP protocol)
# -P: Port
# -r: Recursive (copy directories)
scp -P $PORT -r "$LOCAL_DIR"/* "$USER@$HOST:$REMOTE_DIR"

echo "=== デプロイが完了しました ==="
