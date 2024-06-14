import os
import zipfile

# 文件夹压缩：压缩
def compress_folder(folder_path, zip_file_path):
    """压缩指定的文件夹到一个ZIP文件中。"""
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_in_zip_path = os.path.relpath(file_path, os.path.dirname(folder_path))
                zipf.write(file_path, file_in_zip_path)

if __name__=="__main__":
    compress_folder("/Users/eports/Desktop/DischargingProgress_EDI", "/Users/eports/Desktop/DischargingProgress_EDI.zip")