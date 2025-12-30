#!/bin/bash

# Configuration
HOST="173.209.32.66"
USER="fxgacz89"
REMOTE_DIR="public_html" # Adjust if your server uses 'www' or root
LOCAL_DIR="/Users/mayukookada/Desktop/DRPwebsite/"

echo "=== Starting Deployment to $HOST (SFTP/SSH) ==="
echo "Local Directory: $LOCAL_DIR"
echo "Remote Directory: $REMOTE_DIR"

# Check if rsync is installed
if ! command -v rsync &> /dev/null; then
    echo "Error: rsync configuration not found."
    exit 1
fi

echo "Connecting..."
echo "Please enter your SSH/FTP password when prompted."

# Run rsync
# -a: Archive mode (preserves permissions, times, etc.)
# -v: Verbose output
# -z: Compress data during transfer
# -e ssh: Use SSH for encrypted transfer (SFTP)
# --exclude: Skip unnecessary files
rsync -avz -e 'ssh -p 27' \
    --exclude '.git' \
    --exclude '.DS_Store' \
    --exclude '*.py' \
    --exclude '*.sh' \
    --exclude 'docs' \
    "$LOCAL_DIR" "$USER@$HOST:$REMOTE_DIR"

echo "=== Deployment Complete ==="
