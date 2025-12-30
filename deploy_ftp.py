import ftplib
import os
import getpass

# FTP Configuration
FTP_HOST = "173.209.32.66"
FTP_USER = "fxgacz89"
LOCAL_DIR = "/Users/mayukookada/Desktop/DRPwebsite"
REMOTE_DIR = "public_html"  # Usually public_html is the root for web content

def upload_files(ftp, local_dir, remote_dir):
    try:
        ftp.cwd(remote_dir)
    except ftplib.error_perm:
        print(f"Creating remote directory: {remote_dir}")
        ftp.mkd(remote_dir)
        ftp.cwd(remote_dir)

    for item in os.listdir(local_dir):
        if item.startswith('.') or item == "__pycache__" or item.endswith(".py"):
            continue

        local_path = os.path.join(local_dir, item)
        
        if os.path.isfile(local_path):
            print(f"Uploading {item}...")
            with open(local_path, 'rb') as f:
                ftp.storbinary(f"STOR {item}", f)
        elif os.path.isdir(local_path):
            print(f"Entering directory {item}...")
            upload_files(ftp, local_path, item)
            ftp.cwd("..")

def main():
    print(f"Deploying to {FTP_HOST} as {FTP_USER}")
    password = getpass.getpass("Enter FTP Password: ")

    try:
        with ftplib.FTP(FTP_HOST) as ftp:
            print("Connecting...")
            ftp.login(user=FTP_USER, passwd=password)
            print("Login successful.")
            
            # Navigate to root directory if needed, or stick to login dir
            # Start upload
            upload_files(ftp, LOCAL_DIR, REMOTE_DIR)
            
            print("Deployment completed successfully!")
            
    except ftplib.all_errors as e:
        print(f"FTP Error: {e}")

if __name__ == "__main__":
    main()
