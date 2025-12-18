import os
import shutil
from uuid import uuid4
from fastapi import UploadFile

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_upload_file(file: UploadFile) -> str:
    file_ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path
